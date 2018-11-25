#!/usr/bin/python3
from flask import Flask, Response, request
import spacy
import json

app = Flask(__name__)

@app.route("/de", methods=['POST'])
def de():
    text = request.form.get('text')
    filterType =  request.form.get('type')
    user_def_tags = request.form.get('user_def_tags')
    if not text or text == '':
        return Response(json.dumps({ "sucess": False, "messages": ["No text submitted!"]}), mimetype='application/json')
    if filterType and not (filterType.upper() in ['PROPN', 'NOUN', 'VERB', 'ADP']):
        return Response(json.dumps({ "sucess": False, "messages": ["Invalid type!"]}), mimetype='application/json')
    # load as german
    nlp = spacy.load('de')
    doc = nlp(text)
    entities = []
    for token in doc:
        if not filterType or (filterType and token.pos_ == filterType.upper()):
            entities.append({
                "text": token.text,
                "lemma": token.lemma_,
                "type": token.pos_,
                'tag': token.tag_,
                'pos': token.pos_
                #'label': token.label,
                #'start': token.start_char,
                #'stop': token.end_char
            })
    resp = {
       "success": True,
       "data": entities,
       "user_def_tags": user_def_tags
    }
    return Response(json.dumps(resp), mimetype='application/json', headers={"Access-Control-Allow-Origin": "*"})


@app.route("/en", methods=['POST'])
def en():
    text = request.form.get('text')
    filterType =  request.form.get('type')
    user_def_tags = request.form.get('user_def_tags')
    if not text or text == '':
        return Response(json.dumps({ "sucess": False, "messages": ["No text submitted!"]}), mimetype='application/json')
    if filterType and not (filterType.upper() in ['PROPN', 'NOUN', 'VERB', 'ADP']):
        return Response(json.dumps({ "sucess": False, "messages": ["Invalid type!"]}), mimetype='application/json')
    # load as english
    nlp = en_core_web_sm.load('')
    doc = nlp(text)
    entities = []
    for token in doc:
        if not filterType or (filterType and token.pos_ == filterType.upper()):
            entities.append({
                "text": token.text,
                "lemma": token.lemma_,
                "type": token.pos_,
                'tag': token.tag_,
                'pos': token.pos_
                #'label': token.label,
                #'start': token.start_char,
                #'stop': token.end_char
            })
    resp = {
       "success": True,
       "data": entities,
       "user_def_tags": user_def_tags
    }
    return Response(json.dumps(resp), mimetype='application/json', headers={"Access-Control-Allow-Origin": "*"})
