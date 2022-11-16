# Machine learning (ML) on a Flask REST API.

## Running

    source env/bin/activate
    pip install -r requirements.txt

    export FLASK_APP=main.py
    export FLASK_RUN_HOST=localhost
    export FLASK_RUN_PORT=4001
    export FLASK_DEBUG=true

    flask run

## Deploy on Google App Engine

    gcloud config set project [app-slug]
    gcloud app deploy app.yaml
