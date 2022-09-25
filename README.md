# PEPE-Sematics

PEPE-Sematics is the productionized version of the PEPE-Model by [Xingyao Wang](https://xingyaoww.github.io/) and [David Jurgens](https://jurgens.people.si.umich.edu/). While the original authors have created a slack extension. Our aim is to create a web app where chats inputted produce a suitable reply to the lastest chat message. This means the semantics of text are understood and then several appropriate meme/gif is presented for the user to choose from.

## Getting Started

To make it easy to get started, a list of recommended next steps 

### Setup 

Standard Workflow:- 

```
git clone https://github.com/Nikhil-Mudgal/PEPE-Semantics.git

```

### Commiting Pradigm 

```
git branch <branch_name>
git add <files_to_add>
git commit "Something_desciptive_yet_compact"
git push 

```
If the request passes tests it gets pushed into the repo. 

## Explanation of the Project

To do..


## Models

### Inference example 
- Local: run `notebooks/retrieve_gifs.ipynb`
- Colab (same as local, just with git clone): [link](https://colab.research.google.com/drive/1wDCRnv8ohWk32JxgRC3Qh4BX9ecfs2_H?usp=sharing)

## Deployment

The model will be deployed into as a web service in GCP (Cloud Run), which will be used as the backend of the web application (Gradio). 

Cloud Run is a service for creating web endpoints from Docker Containers. The elements required to use this service are: 

1. A source code with the functions for inference.
    - In the case of our project it is the `scripts` and `src` folders as well as the `main.py` file. 
    - The `scripts` folder contains python modules to download the artifact's model (weights) as well as pre-computed gif embeddings (vector representations of images). 
    - The `src` folder defines how the model is actually used during inference, as well as a `config.py` file that is actually used by files within `scripts`
    - The `main.py` file is a basic Flask API. In the GET method it returns a simple sentence, and with POST method it receives a sentence (string) and produces a gif URL.
2. A `Dockerfile`
    - Where we define the essential elements for the application to work.
    - It is worth mention, that we follow the same steps shown in the colab notebook (see above), that is
        - first we pip install requirements,
        - install the local package for inference (in `src`),
        - download model artifacts, data for indexation of images, and build the index with FAIS
        - and finally, we run the Flask application
3. Additional files
    - `requirements.txt` for env setup
    - `setup.py` to install custom package (`pepe_semantics` defined in `src`)
    - Ignore files:
        - `.gitignore` to control tracking some files
        - `.dockerignore` so the docker container doesn't contain useless files
        - `.gcloudignore` so useless files are not uploaded to GCP Run

### Manual deployment

1. Clone this repository in local environment or within the provided GCP Shell (easier)
2. CD into the directory
3. Create a GCP Artifact repository. This step should be done onlye ONCE:
    - `gcloud artifacts repositories create <REPOSITORY_NAME> --repository-format=docker --location=us-central1 --description="Docker repository"`
    - e.g. `gcloud artifacts repositories create pepe-semantics --repository-format=docker --location=us-central1 --description="Docker repository"`
4. Run the bash script: `gcp_deploy.sh`
    - `sh ./gcp_deploy.sh [APP_NAME] [IMAGE_NAME] [TAG]`
    - e.g. `sh ./gcp_deploy.sh pepe-semantics pepe-semantics-rev1 dev`

Once this is done we can go to Cloud Run console and verify the service is up and running. It can take some time until the service gets in-service, we can see the state of the container in Cloud Run -> Logs.

For more information for how this setup came to be, see: 

[YouTube video](https://www.youtube.com/watch?v=FPFDg5znLTM&list=PLY91jl6VVD7wLP84OUgmjGSUBbem92KHk&index=3&ab_channel=FedericoTartarini)

### Continuous Deployment

To implement Continuous Deployment in GCP we can use GitHub actions to trigger a similar set of commands as the ones above but managed by a GitHub instance.

The instructions followed to setup GitHub actions are shown here:

[YouTube video](https://www.youtube.com/watch?v=NCa0RTSUEFQ&list=PLY91jl6VVD7wLP84OUgmjGSUBbem92KHk&index=8&ab_channel=FedericoTartarini)



## Contributors 

Reach out to us at:-

* [Brendon]
* [Job]
* [Nikhil-Mudgal](https://github.com/Nikhil-Mudgal) -- nmudgal1106@gmail.com
* [Parth]
* [Renat]


