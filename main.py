#!/usr/bin/env python
# encoding: utf-8

import json

from flask import Flask, request
from transformers import pipeline

app = Flask(__name__)

ner_pipeline = pipeline(model="KBLab/bert-base-swedish-cased-ner", task="ner")

@app.route('/')
def index():
  text = "Tom bor på Södermalm och han är 45 år."
  print("NER:", ner_pipeline(text))
  result = map(lambda entity: entity | { "score": float(entity['score']) }, ner_pipeline(text))
  print(result)
  return json.dumps({'entities': list(result)})
