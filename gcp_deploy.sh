#!/bin/bash

if test "$#" -ne 3; then
   echo "Usage: ./gcp_deploy.sh app_name image_name tag"
   echo "   eg: ./gcp_deploy.sh pepe_semantics pepe_sem_faster dev"
   exit
fi

APP_NAME=$1
IMAGE_NAME=$2
TAG=$3

PROJECT=$(gcloud config get-value project)
REPOSITORY_NAME=pepe-semantics

# Submit a docker building tasks
gcloud builds submit "." --region=us-central1 --tag us-central1-docker.pkg.dev/$PROJECT/$REPOSITORY_NAME/$IMAGE_NAME:$TAG

# Deploy
gcloud run deploy $APP_NAME --image us-central1-docker.pkg.dev/$PROJECT/$REPOSITORY_NAME/$IMAGE_NAME:$TAG --region=us-central1 --allow-unauthenticated