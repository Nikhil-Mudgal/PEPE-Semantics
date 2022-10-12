### Deployment steps

**Step 1** (Only done once, do not run again):

```
gcloud artifacts repositories create streamlit --repository-format=docker --location=us-central1 --description="Streamlit apps"
```

### Manual process

**Step 2** 

```
gcloud builds submit . --region=us-central1 --tag us-central1-docker.pkg.dev/smooth-calling-362915/streamlit/frontend2:dev
```

**Step 3**

Change X in pepe-front-X for a number:

```
gcloud run deploy pepe-frontend --image us-central1-docker.pkg.dev/smooth-calling-362915/streamlit/pepe-front-X:dev --region=us-central1 --allow-unauthenticated
```

### Automatic

Change number of rev for 2,3...

```
sh ./gcp_deploy.sh pepe-frontend pepe-front-rev1 dev
```

