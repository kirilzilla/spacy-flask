#!/usr/bin/python3
from flask import Flask, Response, request
import spacy
import json

app = Flask(__name__)

@app.route("/de", methods=['DE'])
def de():
    text = request.form.get('text')
    filterType =  request.form.get('type')
    #if not text or text == '':
    #    return Response(json.dumps({ "sucess": False, "messages": ["No text submitted!"]}), mimetype='application/json')
    #if filterType and not (filterType.upper() in ['PROPN', 'NOUN', 'VERB', 'ADP']):
    #    return Response(json.dumps({ "sucess": False, "messages": ["Invalid type!"]}), mimetype='application/json')
    # load as german
    nlp = spacy.load('de')
    doc = nlp(request.form['text'])
    entities = []
    for token in doc:
        if not filterType or (filterType and token.pos_ == filterType.upper()):
            entities.append({
                "text": token.text,
                "lemma": token.lemma_,
                "type": token.pos_,
                'tag': token.tag_,
                'pos': token.pos_,
                'start': token.start_char,
                'stop': token.end_char
            })
    resp = {
       "success": True,
       "data": entities
    }
    return Response(json.dumps(resp), mimetype='application/json', headers={"Access-Control-Allow-Origin": "*"})


@app.route("/en", methods=['POST'])
def en():
    text = request.form.get('text')
    filterType =  request.form.get('type')
    if not text or text == '':
        return Response(json.dumps({ "sucess": False, "messages": ["No text submitted!"]}), mimetype='application/json')
    if filterType and not (filterType.upper() in ['PROPN', 'NOUN', 'VERB', 'ADP']):
        return Response(json.dumps({ "sucess": False, "messages": ["Invalid type!"]}), mimetype='application/json')
    # load as english
    nlp = spacy.load('en')
    doc = nlp(text)
    entities = []
    for token in doc:
        # if token.pos_=='NOUN':
        if not filterType or (filterType and token.pos_ == filterType.upper()):
            entities.append({
                "text": token.text,
                "lemma": token.lemma_,
                "type": token.pos_,
                'tag': token.tag_,
                'pos': token.pos_,
                'start': token.start_char,
                'stop': token.end_char
            })
    resp = {
       "success": True,
       "data": entities
    }
    return Response(json.dumps(resp), mimetype='application/json', headers={"Access-Control-Allow-Origin": "*"})
