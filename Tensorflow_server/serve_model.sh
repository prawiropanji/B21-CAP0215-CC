#! /bin/bash

# this script is execute bellow command for running the tensorflow-model server

nohup tensorflow_model_server \
--rest_api_port=8501 \
--model_name=<name-your-model-here> \
--model_base_path= <your-path-to-savedmodel> > server.log 2>&1