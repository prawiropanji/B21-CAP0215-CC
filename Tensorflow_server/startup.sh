#! /bin/bash
# this startup script for insatall all dependencies need for running tensorflow model server
# this will runing after creation new VM instances

apt-get update
apt-get install -y python3
apt-get install -y python3-pip
echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | sudo tee /etc/apt/sources.list.d/tensorflow-serving.list && curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | sudo apt-key add -
sudo apt-get update && sudo apt-get install -y tensorflow-model-server