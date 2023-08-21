#!/bin/bash

set -xe

NAME=devan_api
PORT_HOST=8080
IMAGE=devan_api:latest

docker run -d --name $NAME -p $PORT_HOST:80 $IMAGE
