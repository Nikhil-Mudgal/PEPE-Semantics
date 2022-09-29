#!/bin/bash

if test "$#" -ne 3; then
   echo "Usage: ./gcp_deploy.sh app_name image_name tag"
   echo "   eg: ./gcp_deploy.sh pepe-semantics pepe-semantics-rev-1 dev"
   exit
fi

APP_NAME=$1
IMAGE_NAME=$2
TAG=$3

PROJECT_ID=$(gcloud config get-value project)
REPOSITORY_NAME=pepe-semantics

# Submit a docker image-building task
# This commands works properly directly on the CLI
#gcloud builds submit . --region=us-central1 --tag us-central1-docker.pkg.dev/$PROJECT/$REPOSITORY_NAME/$IMAGE_NAME:$TAG
#gcloud builds submit --region=us-central1 --tag us-central1-docker.pkg.dev/$PROJECT/$REPOSITORY_NAME/$IMAGE_NAME:$TAG
# This commands works better when called from a bash script
gcloud builds submit --config=cloudbuild.yaml --substitutions=REPO_NAME=$REPOSITORY_NAME,TAG_NAME=$TAG,REVISION_ID=$IMAGE_NAME

# Deploy
gcloud run deploy $APP_NAME --image us-central1-docker.pkg.dev/$PROJECT_ID/$REPOSITORY_NAME/$IMAGE_NAME:$TAG --region=us-central1 --allow-unauthenticated --memory=4Gi