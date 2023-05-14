import os
from flask import Flask, request, redirect, jsonify, abort, make_response, Response, send_file, session
from flask_restful import Resource, Api,reqparse
import requests
import json

PATH = '../DB'
#PATH = '.'


class GetUser(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        username = someJson.get('username')

        with open(f'{PATH}/user.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        keys = ar.keys()
        if username not in keys:
            resp = jsonify({'error':'username is not valid'})
            resp.status_code = 401
            return resp
        
        resp = jsonify({'info': ar[username]})
        resp.status_code = 200
        return resp


class AddUser(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        username = someJson.get('username')
        password = someJson.get('password')
        user_type = someJson.get('user_type')
        balance = 0
        builds_created = []
        compliments = 0
        warnings = 0
        account_is_active = 'True'
        _10off = 'False'
        position = 0

        with open(f'{PATH}/user.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        keys = ar.keys()
        if username in keys:
            resp = jsonify({'error':'username is taken'})
            resp.status_code = 401
            return resp
        ar[username] = {'username': username, 'password': password, 'user_type': user_type, 'balance': balance, 'builds_created': builds_created, \
                        'compliments': compliments, 'warnings': warnings, 'account_is_active': account_is_active, '_10off': _10off, 'position': position}
        
        with open('user.csv','w') as csvfile:
            csvfile.write(str(ar))
        
        resp = jsonify({'info':'user added'})
        resp.status_code = 200
        return resp


class UpdateUser(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        username = someJson.get('username')
        attribute = someJson.get('attribute')
        value = someJson.get('value')

        with open(f'{PATH}/user.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        keys = ar.keys()
        if username not in keys:
            resp = jsonify({'error':'username is not valid'})
            resp.status_code = 401
            return resp
        
        if attribute == 'builds_created':
            ar[username][attribute].append(value)
        elif attribute == 'compliments' or attribute == 'warnings':
            ar[username][attribute] = int(ar[username][attribute]) + value
            ar[username]['position'] = (int(ar[username]['compliments']) - int(ar[username]['warnings'])) / 3
        else:
            ar[username][attribute] = value
        
        with open(f'{PATH}/user.csv','w') as csvfile:
            csvfile.write(str(ar))
        resp = jsonify({'info': 'user attribute changed'})
        resp.status_code = 200
        return resp


class GetForm(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        form_id = someJson.get('form_id')

        with open(f'{PATH}/form.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        keys = ar.keys()
        if form_id not in keys:
            resp = jsonify({'error':'form_id is not valid'})
            resp.status_code = 401
            return resp
        
        resp = jsonify({'info': ar[form_id]})
        resp.status_code = 200
        return resp


class AddForm(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        form_id = someJson.get('form_id')
        filled_by = someJson.get('filled_by')
        filled_for = someJson.get('filled_for')
        text = someJson.get('text')
        type = someJson.get('type')
        status = someJson.get('status')

        with open(f'{PATH}/form.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        keys = ar.keys()
        if form_id in keys:
            resp = jsonify({'error':'form_id is taken'})
            resp.status_code = 401
            return resp
        ar[form_id] = {'form_id': form_id, 'filled_by': filled_by, 'filled_for': filled_for, 'text': text, 'type': type, 'status': status}
        
        with open(f'{PATH}/form.csv','w') as csvfile:
            csvfile.write(str(ar))
        
        resp = jsonify({'info':'form added'})
        resp.status_code = 200
        return resp


class UpdateForm(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        form_id = someJson.get('form_id')
        attribute = someJson.get('attribute')
        value = someJson.get('value')

        with open(f'{PATH}/form.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        keys = ar.keys()
        if form_id not in keys:
            resp = jsonify({'error':'form_id is not valid'})
            resp.status_code = 401
            return resp
        
        ar[form_id][attribute] = value
        
        with open(f'{PATH}/form.csv','w') as csvfile:
            csvfile.write(str(ar))
        resp = jsonify({'info': 'form attribute changed'})
        resp.status_code = 200
        return resp


class GetForm(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        form_id = someJson.get('form_id')

        with open(f'{PATH}/form.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        keys = ar.keys()
        if form_id not in keys:
            resp = jsonify({'error':'form_id is not valid'})
            resp.status_code = 401
            return resp
        
        resp = jsonify({'info': ar[form_id]})
        resp.status_code = 200
        return resp



apis = Flask(__name__)
api = Api(apis, prefix="")
api.add_resource(AddUser, '/user/add', strict_slashes=False)
api.add_resource(GetUser, '/user/get', strict_slashes=False)
api.add_resource(UpdateUser, '/user/update', strict_slashes=False)
api.add_resource(AddForm, '/form/add', strict_slashes=False)
api.add_resource(GetForm, '/form/get', strict_slashes=False)
api.add_resource(UpdateForm, '/form/update', strict_slashes=False)
