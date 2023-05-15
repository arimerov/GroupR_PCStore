import os
from flask import Flask, request, redirect, jsonify, abort, make_response, Response, send_file, session
from flask_restful import Resource, Api,reqparse
import requests
import json

#PATH = '../DB'
PATH = '.'


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
        user_email = someJson.get('user_email')
        balance = 0
        builds_created = []
        compliments = 0
        warnings = 0
        account_is_active = 'True'
        _10off = 'False'
        position = 0
        logged_in = 'False'

        with open(f'{PATH}/user.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        keys = ar.keys()
        if username in keys:
            resp = jsonify({'error':'username is taken'})
            resp.status_code = 401
            return resp
        ar[username] = {'username': username, 'password': password, 'user_type': user_type, 'balance': balance, 'builds_created': builds_created, 'user_email': user_email, \
                        'compliments': compliments, 'warnings': warnings, 'account_is_active': account_is_active, '_10off': _10off, 'position': position, 'logged_in': logged_in}
        
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
        
        # if attribute == 'builds_created':
        #     ar[username][attribute].append(value)
        # elif attribute == 'compliments' or attribute == 'warnings':
        #     ar[username][attribute] = int(ar[username][attribute]) + value
        #     ar[username]['position'] = (int(ar[username]['compliments']) - int(ar[username]['warnings'])) / 3
        # else:
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


class GetPCPart(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        part_id = someJson.get('part_id')

        with open(f'{PATH}/pc_part.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        keys = ar.keys()
        if part_id not in keys:
            resp = jsonify({'error':'part_id is not valid'})
            resp.status_code = 401
            return resp
        
        resp = jsonify({'info': ar[part_id]})
        resp.status_code = 200
        return resp


class AddPCPart(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        part_id = someJson.get('part_id')
        compatibility = someJson.get('compatibility')
        name = someJson.get('name')
        price = someJson.get('price')

        with open(f'{PATH}/pc_part.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        keys = ar.keys()
        if part_id in keys:
            resp = jsonify({'error':'part_id is taken'})
            resp.status_code = 401
            return resp
        ar[part_id] = {'part_id': part_id, 'compatibility': compatibility, 'name': name, 'price': price}
        
        with open(f'{PATH}/pc_part.csv','w') as csvfile:
            csvfile.write(str(ar))
        
        resp = jsonify({'info':'form added'})
        resp.status_code = 200
        return resp


class UpdatePCPart(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        part_id = someJson.get('part_id')
        attribute = someJson.get('attribute')
        value = someJson.get('value')

        with open(f'{PATH}/pc_part.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        keys = ar.keys()
        if part_id not in keys:
            resp = jsonify({'error':'part_id is not valid'})
            resp.status_code = 401
            return resp
        
        ar[part_id][attribute] = value
        
        with open(f'{PATH}/pc_part.csv','w') as csvfile:
            csvfile.write(str(ar))
        resp = jsonify({'info': 'pc_part attribute changed'})
        resp.status_code = 200
        return resp


class GetBuild(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        build_id = someJson.get('build_id')

        with open(f'{PATH}/pc_build.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        keys = ar.keys()
        if build_id not in keys:
            resp = jsonify({'error':'build_id is not valid'})
            resp.status_code = 401
            return resp
        
        resp = jsonify({'info': ar[build_id]})
        resp.status_code = 200
        return resp


class AddBuild(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        build_id = someJson.get('build_id')
        rating = someJson.get('rating')
        name = someJson.get('name')
        comments = someJson.get('comments')
        parts = someJson.get('parts')
        
        price = 0
        with open(f'{PATH}/pc_part.csv','r') as csvfile:
            ar_parts = csvfile.read()
        ar_parts = eval(ar_parts)
        for i in parts:
            price += int(ar_parts[i]['price'])

        with open(f'{PATH}/pc_build.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        keys = ar.keys()
        if build_id in keys:
            resp = jsonify({'error':'build_id is taken'})
            resp.status_code = 401
            return resp
        ar[build_id] = {'build_id': build_id, 'rating': rating, 'name': name, 'price': price, 'comments': comments, 'parts': parts}
        
        with open(f'{PATH}/pc_build.csv','w') as csvfile:
            csvfile.write(str(ar))
        
        resp = jsonify({'info':'form added'})
        resp.status_code = 200
        return resp


class UpdateBuild(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        build_id = someJson.get('build_id')
        attribute = someJson.get('attribute')
        value = someJson.get('value')

        with open(f'{PATH}/pc_build.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        keys = ar.keys()
        if build_id not in keys:
            resp = jsonify({'error':'build_id is not valid'})
            resp.status_code = 401
            return resp
        
        ar[build_id][attribute] = value
        
        with open(f'{PATH}/pc_build.csv','w') as csvfile:
            csvfile.write(str(ar))
        resp = jsonify({'info': 'pc_build attribute changed'})
        resp.status_code = 200
        return resp


apis = Flask(__name__)
api = Api(apis)
api.add_resource(AddUser, '/user/add', strict_slashes=False)
api.add_resource(GetUser, '/user/get', strict_slashes=False)
api.add_resource(UpdateUser, '/user/update', strict_slashes=False)
api.add_resource(AddForm, '/form/add', strict_slashes=False)
api.add_resource(GetForm, '/form/get', strict_slashes=False)
api.add_resource(UpdateForm, '/form/update', strict_slashes=False)
api.add_resource(AddPCPart, '/part/add', strict_slashes=False)
api.add_resource(GetPCPart, '/part/get', strict_slashes=False)
api.add_resource(UpdatePCPart, '/part/update', strict_slashes=False)
api.add_resource(AddBuild, '/build/add', strict_slashes=False)
api.add_resource(GetBuild, '/build/get', strict_slashes=False)
api.add_resource(UpdateBuild, '/build/update', strict_slashes=False)