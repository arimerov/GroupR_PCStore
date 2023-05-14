import os
from flask import Flask, request, redirect, jsonify, abort, make_response, Response, send_file, session
from flask_restful import Resource, Api,reqparse
import requests
import json


api_route = 'http://127.0.0.1:8001'


def add_user_to_db(username, password, user_type):
    body = {'username': username, "password": password, "user_type": user_type}
    req_url = f'{api_route}/user/add'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data


def get_user_from_db(username):
    body = {'username': username}
    req_url = f'{api_route}/user/get'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data


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


def add_form_to_db(form_id, filled_by, filled_for, text, type, status):
    body = {'form_id': form_id, "filled_by": filled_by, "filled_for": filled_for, "text": text, "type": type, "status": status}
    req_url = f'{api_route}/form/add'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data


def get_form_from_db(form_id):
    body = {'form_id': form_id}
    req_url = f'{api_route}/form/get'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data


def update_form_in_db(form_id, filled_by, filled_for, text, type, status):
    body = {'form_id': form_id, "filled_by": filled_by, "filled_for": filled_for, "text": text, "type": type, "status": status}
    req_url = f'{api_route}/form/update'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data


def add_part_to_db(part_id, compatibility, name, price):
    body = {'part_id': part_id, "compatibility": compatibility, "name": name, "price": price}
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


def add_build_to_db(build_id, rating, name, comments, parts):
    body = {'build_id': build_id, "rating": rating, "name": name, "comments": comments, "parts": parts}
    req_url = f'{api_route}/build/add'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
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