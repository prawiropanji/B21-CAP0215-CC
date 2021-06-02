#! /bin/bash
# this startup script for insatall all dependencies need for running Prediction API
# this will runing after creation new VM instances

apt-get update
apt-get install -y python3
apt-get install -y python3-pip