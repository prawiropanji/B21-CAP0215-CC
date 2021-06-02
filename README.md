# B21-CAP0215-CC

### Cloud Computing Backend and Deployment for B21-CAP0215 Capstone Project 2021

Welcome to cloud computing `README` :smiley: .

# About The Project

here i will tell you all the step that i do in my `Skindec` application Capstone Project that help identify user of their health facial skin with android appliaction as a cloud computing team.

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
