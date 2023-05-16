import os
from flask import Flask, request, redirect, jsonify, abort, make_response, Response, send_file, session
from flask_restful import Resource, Api,reqparse
import requests
import json
from flask_cors import CORS


api_route = 'http://127.0.0.1:8001'

def add_user_to_db(username, password, user_type, user_email, firstname, lastname):
    body = {'username': username, "password": password, "user_type": user_type, "user_email": user_email, "firstname": firstname, "lastname": lastname}
    req_url = f'{api_route}/user/add'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data


def get_user_from_db(username):
    print("get_user_from_db()")
    body = {'username': username}
    req_url = f'{api_route}/user/get'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    return r_json


def update_user_in_db(username, attribute, value):
    body = {'username': username, 'attribute': attribute, 'value': value}
    req_url = f'{api_route}/user/update'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data


def add_forum_to_db(filled_by, filled_for, text, type, status):
    body = {"filled_by": filled_by, "filled_for": filled_for, "text": text, "type": type, "status": status}
    req_url = f'{api_route}/forum/add'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data


def get_forum_from_db(forum_id):
    body = {'forum_id': forum_id}
    req_url = f'{api_route}/forum/get'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data


def get_forums_from_db():
    req_url = f'{api_route}/forums/get'
    r = requests.post(req_url)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    keys = data.keys()
    ar = []
    for i in keys:
        ar.append(data[i])
    return ar


def update_forum_in_db(forum_id, attribute, value):
    body = {'forum_id': forum_id, "attribute": attribute, "value": value}
    req_url = f'{api_route}/forum/update'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data


def add_part_to_db(part_id, part_type, compatibility, name, price):
    body = {'part_id': part_id, "part_type": part_type, "compatibility": compatibility, "name": name, "price": price}
    req_url = f'{api_route}/part/add'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data


def get_part_from_db(part_id):
    body = {'part_id': part_id}
    req_url = f'{api_route}/part/get'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data


def get_parts_from_db():
    req_url = f'{api_route}/parts/get'
    r = requests.post(req_url)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data


def update_part_in_db(part_id, compatibility, name, price):
    body = {'part_id': part_id, "compatibility": compatibility, "name": name, "price": price}
    req_url = f'{api_route}/part/update'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data


def add_build_to_db(rating, comments, parts):
    body = {"rating": rating, "comments": comments, "parts": parts}
    req_url = f'{api_route}/build/add'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data


def get_builds_from_db():
    req_url = f'{api_route}/builds/get'
    r = requests.post(req_url)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    keys = data.keys()
    ar = []
    for i in keys:
        ar.append(data[i])
    return data


def get_build_from_db(build_id):
    body = {'build_id': build_id}
    req_url = f'{api_route}/build/get'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data


def update_part_in_db(build_id, rating, name, comments, parts):
    body = {'build_id': build_id, "rating": rating, "name": name, "comments": comments, "parts": parts}
    req_url = f'{api_route}/build/update'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data

# a = add_user_to_db('Alex', '123', 'admin')
# print(a)

# b = get_user_from_db('georgy')
# print(b)

# c = update_user_in_db('georgy', 'compliments', 1)
# print(c)