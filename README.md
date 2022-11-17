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

    curl "http://localhost:4001/?text=Tom%20bor%20i%20Stockholm%20och%20han%20%C3%A4r%2045%20%C3%A5r."

Response:

    {
      "entities":[
        { "entity":"PER", "score":0.999692440032959, "index":1, "word":"Tom", "start":0, "end":3 },
        { "entity":"LOC", "score":0.9984962940216064, "index":4, "word":"S\u00f6dermalm", "start":11, "end":20 },
        { "entity":"MSR", "score":0.9974410533905029, "index":8, "word":"42", "start":32, "end":34 },
        { "entity":"MSR", "score":0.9969724416732788, "index":9, "word":"\u00e5r", "start":35, "end":37 }
      ]
    }

## Deploy on Google App Engine

    gcloud config set project [app-slug]
    gcloud app deploy app.yaml
