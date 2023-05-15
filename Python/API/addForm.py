import os
from flask import Flask, request, redirect, jsonify, abort, make_response, Response, send_file, session
from flask_restful import Resource, Api,reqparse
import requests
import json


api_route = 'http://127.0.0.1:8001'

def add_form(form_id, filled_by, filled_for, text, type, status):
    body = {'form_id': form_id, "filled_by": filled_by, "filled_for": filled_for, "text": text, "type": type, "status": status}
    req_url = f'{api_route}/form/add'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data

a = add_form('1', 'georgy', 'alex', 'text', 'test', 0)
print(a)
