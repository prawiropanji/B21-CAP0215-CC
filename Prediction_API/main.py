from flask import Flask, render_template, request, jsonify
from flask_uploads import configure_uploads, IMAGES, UploadSet
import json
import requests
from keras.preprocessing import image
import numpy as np

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'images/'
configure_uploads(app, photos)

@app.route('/upload', methods=['POST'])
def upload():
    filename = photos.save(request.files['file'])
    
    image_name = f"images/{filename}" #change it to your filename
    img = image.load_img(image_name, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    image_data = np.vstack([x])
    
    data = json.dumps({"signature_name":"serving_default", "instances": image_data.tolist()})
    headers = {"content-type": "application/json"}
    json_response = requests.post('http://10.184.0.2:8501/v1/models/skindec:predict', data=data, headers=headers)
    r = json_response.json()

    predict = r["predictions"][0]

    if predict[0] == 1:
        result = "acne"
    elif predict[1] == 1:
        result = "dry"
    elif predict[2] == 1:
        result = "normal"
    elif predict[3] == 1:
        result = "oily"
    elif predict[4] == 1:
        result = "scar"

    return jsonify({"prediction" : result})
    
if __name__ == "__main__":
    app.run(host="10.184.0.3", port=5000)
