#! /bin/bash

# this script is execute bellow command for running the tensorflow-model server

nohup tensorflow_model_server \
--rest_api_port=8501 \
--model_name=skindec \
--model_base_path=/home/c0070657/tensorflow_serve/saved_model > server.log 2>&1