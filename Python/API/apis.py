import os
from flask import Flask, request, redirect, jsonify, abort, make_response, Response, send_file, session
from flask_restful import Resource, Api,reqparse
import requests
import json

PATH = '../../DB'
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
        user_email = someJson.get('user_email')
        firstname = someJson.get('firstname')
        lastname = someJson.get('lastname')
        balance = 0
        builds_created = []
        builds_purchased = []
        compliments = 0
        warnings = 0
        account_is_active = 'True'
        _10off = 'False'
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
                        'compliments': compliments, 'warnings': warnings, 'account_is_active': account_is_active, '_10off': _10off, 'firstname': firstname, \
                            'lastname': lastname, 'logged_in': logged_in, 'builds_purchased': builds_purchased}
        
        with open(f'{PATH}/user.csv','w') as csvfile:
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


class GetForum(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        forum_id = someJson.get('forum_id')

        with open(f'{PATH}/forum.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        keys = ar.keys()
        if forum_id not in keys:
            resp = jsonify({'error':'forum_id is not valid'})
            resp.status_code = 401
            return resp
        
        resp = jsonify({'info': ar[forum_id]})
        resp.status_code = 200
        return resp


class GetForums(Resource):
    def post(self):

        with open(f'{PATH}/forum.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        resp = jsonify({'info': ar})
        resp.status_code = 200
        return resp


class AddForum(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        # forum_id = someJson.get('forum_id')
        filled_by = someJson.get('filled_by')
        filled_for = someJson.get('filled_for')
        text = someJson.get('text')
        type = someJson.get('type')
        status = someJson.get('status')

        with open(f'{PATH}/forum.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        keys = ar.keys()
        forum_id = '0' * (5 - len(str(len(keys) + 1))) + str(len(keys) + 1)
        # if forum_id in keys:
        #     resp = jsonify({'error':'forum_id is taken'})
        #     resp.status_code = 401
        #     return resp
        ar[forum_id] = {'forum_id': forum_id, 'filled_by': filled_by, 'filled_for': filled_for, 'text': text, 'type': type, 'status': status}
        
        with open(f'{PATH}/forum.csv','w') as csvfile:
            csvfile.write(str(ar))
        
        resp = jsonify({'info':'forum added'})
        resp.status_code = 200
        return resp


class UpdateForum(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        forum_id = someJson.get('forum_id')
        attribute = someJson.get('attribute')
        value = someJson.get('value')

        with open(f'{PATH}/forum.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        keys = ar.keys()
        if forum_id not in keys:
            resp = jsonify({'error':'forum_id is not valid'})
            resp.status_code = 401
            return resp
        
        ar[forum_id][attribute] = value
        
        with open(f'{PATH}/forum.csv','w') as csvfile:
            csvfile.write(str(ar))
        resp = jsonify({'info': 'forum attribute changed'})
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


class GetParts(Resource):
    def post(self):

        with open(f'{PATH}/pc_part.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        resp = jsonify({'info': ar})
        resp.status_code = 200
        return resp


class AddPCPart(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        part_id = someJson.get('part_id')
        part_type = someJson.get('part_type')
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
        ar[part_id] = {'part_id': part_id, 'compatibility': compatibility, 'name': name, 'price': price, 'part_type': part_type}
        
        with open(f'{PATH}/pc_part.csv','w') as csvfile:
            csvfile.write(str(ar))
        
        resp = jsonify({'info':'forum added'})
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


class GetBuilds(Resource):
    def post(self):

        with open(f'{PATH}/pc_build.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        
        resp = jsonify({'info': ar})
        resp.status_code = 200
        return resp


class AddBuild(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        # build_id = someJson.get('build_id')
        rating = someJson.get('rating')
        comments = someJson.get('comments')
        parts = someJson.get('parts')

        
        price = 0
        with open(f'{PATH}/pc_part.csv','r') as csvfile:
            ar_parts = csvfile.read()
        ar_parts = eval(ar_parts)
        for i in parts:
            price += float(ar_parts[i]['price'])

        with open(f'{PATH}/pc_build.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        keys = ar.keys()
        build_id = '0' * (5 - len(str(len(keys) + 1))) + str(len(keys) + 1)
        # if build_id in keys:
        #     resp = jsonify({'error':'build_id is taken'})
        #     resp.status_code = 401
        #     return resp
        ar[build_id] = {'build_id': build_id, 'rating': rating, 'price': price, 'comments': comments, 'parts': parts}
        print(ar)
        
        with open(f'{PATH}/pc_build.csv','w') as csvfile:
            csvfile.write(str(ar))
        
        resp = jsonify({'info':'forum added'})
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


class RemoveBuild(Resource):
    def post(self):
        someJson = request.get_json(force=True)
        build_id = someJson.get('build_id')

        with open(f'{PATH}/pc_build.csv','r') as csvfile:
            ar = csvfile.read()
        ar = eval(ar)
        del ar[build_id]
        
        with open(f'{PATH}/pc_build.csv','w') as csvfile:
            csvfile.write(str(ar))
        resp = jsonify({'info': 'pc_build deleted'})
        resp.status_code = 200
        return resp



apis = Flask(__name__)
api = Api(apis)
api.add_resource(AddUser, '/user/add', strict_slashes=False)
api.add_resource(GetUser, '/user/get', strict_slashes=False)
api.add_resource(UpdateUser, '/user/update', strict_slashes=False)
api.add_resource(AddForum, '/forum/add', strict_slashes=False)
api.add_resource(GetForum, '/forum/get', strict_slashes=False)
api.add_resource(GetForums, '/forums/get', strict_slashes=False)
api.add_resource(UpdateForum, '/forum/update', strict_slashes=False)
api.add_resource(AddPCPart, '/part/add', strict_slashes=False)
api.add_resource(GetPCPart, '/part/get', strict_slashes=False)
api.add_resource(GetParts, '/parts/get', strict_slashes=False)
api.add_resource(UpdatePCPart, '/part/update', strict_slashes=False)
api.add_resource(AddBuild, '/build/add', strict_slashes=False)
api.add_resource(RemoveBuild, '/build/remove', strict_slashes=False)
api.add_resource(GetBuild, '/build/get', strict_slashes=False)
api.add_resource(GetBuilds, '/builds/get', strict_slashes=False)
api.add_resource(UpdateBuild, '/build/update', strict_slashes=False)