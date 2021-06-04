<h1 align="center">
    SkinDec  
</h1>

<h5 align="center">
    Mobile Development B21-CAP0215 Capstone Project | Healthcare
</h5>

<p align="center">
  <a href="http://developer.android.com/index.html"><img alt="Platform" src="https://img.shields.io/badge/platform-Android-green.svg"></a>
  <a href="http://kotlinlang.org"><img alt="Kotlin" src="https://img.shields.io/badge/kotlin-1.5.0-blue.svg"></a>
  <a href="https://developer.android.com/studio/releases/gradle-plugin"><img alt="Gradle" src="https://img.shields.io/badge/gradle-4.2.1-yellow.svg"></a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/wahyurama-creator/B21-CAP0215-MD/master/assets/thumbnail.png" max-width="1072px" max-height="768px"/>
</p>

## Table of Contents

- [Introduction](#introduction)
- [Technology](#technology)
- [Design Application](#design-application)

## Introduction

At Capstone Project Bangkit 2021, we come up with an idea to create a healthcare themed project. we name our application `SkinDec`. This application was developed to help people identify their facial skintype using their smartphone camera, to provide more information how to properly take care of their skin. three different learning path team developed and contributed to working on this project, B21-CAP0215-MD (Mobile Development), B21-CAP0215-ML (Machine Learning), and B21-CAP0215-CC (Cloud Computing)



## Technology

We combine technologies including Machine Learning, Cloud Computing, and Mobile Development.

<h3>Machine Learning</h3>

    We started looking for datasets according to the labels defined by our team and then built a Machine Learning model with TensorFlow and Keras Neural Network from scratch,
    applying Image Augmentation to our image datasets to expand our dataset so that there is no overwriting and our model generalizes well. Then we tried to optimize our TF model by dropping
    some layers and using Transfer Learning which can drastically improve the accuracy of our model. For deployment, we use TF Serve on our cloud servers.

<h6>&emsp;Library and Framework :</h6>

- [TensorFlow: 2.5.0](https://www.tensorflow.org/api_docs)
- [NumPy: 1.20.3](https://numpy.org/doc/)
- [Keras: 2.4.3](https://keras.io/)

<h3>Cloud Computing</h3>

    Develop API with python programming languange that utilize flask framework and SQLAlchemy extension library to facilitate the comunication between python programs
    and databases and to comunicate with Machine Learning model server.

    We release,manage, and maintain all backend services in the Google Cloud Platform. We deploy our database with SQL Cloud for MYSQL solution, Deploy Machine Learning model
    using TF Serve implementation on Compute Engine solution, Deploy database API on App Engine standard environment, and deploy prediction machine learning model API on Compute Engine solution.

<h6>&emsp;Library and Framework :</h6>

- [Flask: 1.1.2](https://flask.palletsprojects.com/en/2.0.x/)
- [SQLAlchemy: 2.4.3](https://www.sqlalchemy.org/)
- [Flask Marshmallow: 0.14.0](https://flask-marshmallow.readthedocs.io/en/latest/)
- [NumPy: 1.20.3](https://numpy.org/doc/)
- [Keras: 2.4.3](https://keras.io/)

<h3>Mobile Development</h3>

    We implement the design from figma into the android studio xml file, in the form of 3 pages, namely: the onboarding page, the data upload page, then the analysis
    results page which is the classification result.

    We implement an API to perform data transactions starting from sending personal data along with uploading a face image to the server, then getting the skin type
    classification results. As well as recommending suggestions for beauty products that are suitable for that skin type using retrofit and okhttp3.

<h6>&emsp;Library and Framework :</h6>

- [Retrofit: 2.9.0](https://github.com/square/retrofit)
- [Okhttp3: 3.11.0](https://github.com/square/okhttp)
- [ImagePicker: 2.0](https://github.com/Dhaval2404/ImagePicker)
- [Glide: 4.12.0](https://bumptech.github.io/glide/)

## Design Application

<h6>
    We are create design and prototyping with <a href="https://www.figma.com/file/Wk2PXze9Cfi4UJfam2ZsCw/SkinDec?node-id=110%3A124">Figma</a>
</h6>

|                                              OnBoarding                                              |                                          Home Upload                                           |                                              Result                                              |
| :--------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------: |
| ![](https://raw.githubusercontent.com/wahyurama-creator/B21-CAP0215-MD/master/assets/OnBoarding.png) | ![](https://raw.githubusercontent.com/wahyurama-creator/B21-CAP0215-MD/master/assets/Home.png) | ![](https://raw.githubusercontent.com/wahyurama-creator/B21-CAP0215-MD/master/assets/Result.png) |

'+

# B21-CAP0215-CC

### Cloud Computing Backend and Deployment for B21-CAP0215 Capstone Project 2021

Welcome to cloud computing `README` :smiley: .

# About The Project

Cloud computing responsible to deploy database server and machine learning model server. we develop and deploy API so that client can comunicate with the servers to manage user's information and getting a prediction.

# Deployment Solution

Below diagram design of backend and deployment in Google Cloud Platform that are needed for **B21-CAP0215 Capstone Project**
![Image of cloud design](https://i.imgur.com/XeUqryn.jpg)

Spesific cloud solution requirements :

- #### Cloud SQL MySQL

  - Machine Type : Standard Custom 4vCPU, 4GB
  - Storage : SSD 10 GB

- APP Engine standard environment

- GCE 2 vm instances:
  - Machine Type : n1-standard-1 (1 vCPU, 3.75 GB memory)
  - Boot disk : debian-10-buster-v20210512, Balanced persistent disk 10 GB

# Getting Started

if you want replicate my step, follow the following steps

## Create User Database Cloud SQL

1. Go to the Cloud SQL Instances page.

2. Select your project and click Continue.

3. Click Create Instance.

4. Click MySQL.

5. Specify Machine Type, Storage according to [this](####cloud-sql-mysql)

6. Click Create

7. Go to Database section on the left pane, then click `CREATE DATABASE` to create a new database

## Deploy API to database App Engine

click [here](https://github.com/prawiropanji/B21-CAP0215-CC/tree/main/Database_API), too take a look resources needed for create API to MySQL Database in App Egnine.

1. move [app.yaml](https://github.com/prawiropanji/B21-CAP0215-CC/blob/main/Database_API/app.yaml), [main.py](https://github.com/prawiropanji/B21-CAP0215-CC/blob/main/Database_API/main.py), and [requirements.txt](https://github.com/prawiropanji/B21-CAP0215-CC/blob/main/Database_API/requirements.txt) to your Cloud Shell

2. Edit the [main.py](https://github.com/prawiropanji/B21-CAP0215-CC/blob/main/Database_API/main.py) to matching your own database connection configuration

3. create table database from [main.py](https://github.com/prawiropanji/B21-CAP0215-CC/blob/main/Database_API/main.py) module by open python intepreter promter, then type (make sure you open terminal in same directory)

```
>>> from main import db
```

```
>>> db.create_all()
```

4. Initialize your App Engine app with your project and choose its region:

```
$ gcloud app create --project=[YOUR_PROJECT_ID]
```

5. Deploy the API by running following command

```
$ gcloud app deploy
```

6. then wait till the magic things happend :wink:

## Deploy Tensorflow Model Server

click [here](https://github.com/prawiropanji/B21-CAP0215-CC/tree/main/Tensorflow_server), too take a look resources needed for Tensorflow Model Server in GCE.

1. Create [startup.sh](https://github.com/prawiropanji/B21-CAP0215-CC/blob/main/Tensorflow_server/startup.sh) file in your Cloud Shell
2. Type following commands to create VM instances

```
$ gcloud compute instances create [YOUR-INSTANCES-NAME] --zone=[YOUR-PEREFER-ZONE] --machine-type=n1-standard-1 --subnet=default  --tags=tensorflow-server --image=debian-10-buster-v20210512 --image-project=debian-cloud --boot-disk-size=10GB --boot-disk-type=pd-balanced  --m --metadata-from-file startup-script=[FILE_PATH_of_startup.sh]
```

3. Create firewall rule by type bellow comand in Cloud Shell, that allow inggres comming to port 8501 where the `server model` listening to

```
$ gcloud compute firewall-rules create allow-to-model-serve --direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:8501 --source-ranges=0.0.0.0/0 --target-tags=tensorflow-server

```

4. SSH your instance that already created

5. Create [requirements.txt](https://github.com/prawiropanji/B21-CAP0215-CC/blob/main/Tensorflow_server/requirements.txt) contain all packages need for running `serve model`

6. install all requiremnts using pip command

```
$ pip3 install -r requirements.txt
```

7. Move the [savedmodel](https://github.com/diapica/B21-CAP0215-ML/tree/main/Model) in this vm instances

8. To running `serve model` run this command

```
$ nohup tensorflow_model_server \
--rest_api_port=8501 \
--model_name=<name-your-model-here> \
--model_base_path= <your-path-to-savedmodel> > server.log 2>&1
```

the problem occur by running `serve model` by doing this, that is the service will stop if we close the vm terminal. so the solution is we must **run command as Systemd Service in this linux vm**.

1. Create [tensorflow-model.service ](https://github.com/prawiropanji/B21-CAP0215-CC/blob/main/Tensorflow_server/tensorflow-model.service)unit file

2. move this unit file to the `/etc/systemd/system` directory.

```
$ sudo mv tensorflow-model.service /etc/systemd/system
```

3. Create [serve_model.sh](https://github.com/prawiropanji/B21-CAP0215-CC/blob/main/Tensorflow_server/serve_model.sh) shell script in the same directory `savedmodel`, then give executable permission to script file by running

```
$ chmod +x serve_model.sh
```

4. run subsequent command to activate the service

```
$ sudo systemctl daemon-reload

$ sudo systemctl enable tensorflow-model.service

$ sudo systemctl start tensorflow-model.service
```

5. close the ssh vm instances terminal, and the command will keep running `serve model` in the background even if the terminal get closed

## Deploy API to make prediction GCE

click [here](https://github.com/prawiropanji/B21-CAP0215-CC/tree/main/Prediction_API), too take a look resources needed for API to make prediction in GCE.

1. Create [startup.sh](https://github.com/prawiropanji/B21-CAP0215-CC/blob/main/Prediction_API/startup.sh) file in your Cloud Shell

2. Create vm instances by running following command

```
$ gcloud compute instances create [YOUR-INSTANCES-NAME] --zone=[YOUR-PEREFER-ZONE] --machine-type=n1-standard-1 --subnet=default  --tags=prediciton-api --image=debian-10-buster-v20210512 --image-project=debian-cloud --boot-disk-size=10GB --boot-disk-type=pd-balanced  --m --metadata-from-file startup-script=[FILE_PATH_of_startup.sh]
```

3. Create firewall rule by type bellow comand in Cloud Shell, so that the client(mobile) can make request to this API server by allowing ingress to tcp port 5000 that the application listening to

```
$ gcloud compute firewall-rules create allow-flask-port --direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:5000 --source-ranges=0.0.0.0/0 --target-tags=prediction-api
```

4. SSH into the VM instances that already created

5. Create [requirements.txt](https://github.com/prawiropanji/B21-CAP0215-CC/blob/main/Prediction_API/requirements.txt) contain all packages need for running the Prediction API application.

6. Install requirements by type this command

```
$ pip3 install -r requirements.txt
```

7. Create [main.py](https://github.com/prawiropanji/B21-CAP0215-CC/blob/main/Prediction_API/main.py) and we will execute this python apps as Systemd Services

8. give executable permission to this app file

```
$ chmod +x main.py
```

9. Create [prediction.service](https://github.com/prawiropanji/B21-CAP0215-CC/blob/main/Prediction_API/prediction.service) and move it to the `etc/sytemd/system` directory

```
$ sudo mv prediction.service etc/sytemd/system
```

10. run subsequent command to activate the service

```
$ sudo systemctl daemon-reload

$ sudo systemctl enable tensorflow-model.service

$ sudo systemctl start tensorflow-model.service
```

11. Close the vm instances terminal, and this app will kepp running ready to take file image request from client (android) then forward it to the tensorflow model server to make prediction create response to the client based on tensorflow model server response.
