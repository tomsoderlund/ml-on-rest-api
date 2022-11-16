# Machine learning (ML) on a Flask REST API

## Running

Install:

    source env/bin/activate
    pip install -r requirements.txt

Configure Flask:

    export FLASK_APP=main.py
    export FLASK_RUN_HOST=localhost
    export FLASK_RUN_PORT=4001
    export FLASK_DEBUG=true

Start up web server:

    flask run

## Testing

    curl http://localhost:4001

Response:

    {"response": [0.9998905658721924, 0.998997151851654, 0.9956401586532593, 0.9943753480911255]}

## Deploy on Google App Engine

    gcloud config set project [app-slug]
    gcloud app deploy app.yaml
