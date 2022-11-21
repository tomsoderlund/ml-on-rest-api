#!/usr/bin/env python
# encoding: utf-8

import json
import os

from flask import Flask, request
from transformers import pipeline

app = Flask(__name__)

# Models from https://huggingface.co/models
ml_model = 'KBLab/bert-base-swedish-cased-ner'
ner_pipeline = pipeline(model=ml_model, task='ner')

@app.route('/')
def index():
  text = request.args.get('text', 'Tom bor i Stockholm och han är 45 år.')
  pipeline_results = ner_pipeline(text)
  print('NER results:', pipeline_results)
  pipeline_results_adjusted = map(lambda entity: entity | { 'score':float(entity['score']) }, pipeline_results)
  print(pipeline_results_adjusted)
  return json.dumps({'entities': list(pipeline_results_adjusted)})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
