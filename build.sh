#!/bin/bash

set -xe

IMAGE_NAME=cezeitar/devan_api:test

# remove container
docker rm -f $IMAGE_NAME

# rebuild image
docker build -t $IMAGE_NAME .