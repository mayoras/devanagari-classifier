#!/bin/bash

set -xe

IMAGE_NAME=devan_api

# remove container
docker rm -f $IMAGE_NAME

# rebuild image
docker build -t $IMAGE_NAME .