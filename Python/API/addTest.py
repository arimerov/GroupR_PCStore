import os
from flask import Flask, request, redirect, jsonify, abort, make_response, Response, send_file, session
from flask_restful import Resource, Api,reqparse
import requests
import json


api_route = 'http://127.0.0.1:8001'




# def add_build_to_db(rating, comments, parts):
#     body = {"rating": rating, "comments": comments, "parts": parts}
#     req_url = f'{api_route}/build/add'
#     r = requests.post(req_url, json=body)
#     r_json = r.json()
#     try:
#         data = r_json['info']
#     except:
#         data = r_json['error']
#     return data


# def get_parts_from_db():
#     req_url = f'{api_route}/parts/get'
#     r = requests.post(req_url)
#     r_json = r.json()
#     try:
#         data = r_json['info']
#     except:
#         data = r_json['error']
#     return data

# #MAKE PC BUILDS

# def addBuild():
#     for j in range(6):
#         parts = []
#         ar = get_parts_from_db()
#         n = '00' + str(j + 1)
#         parts.append(n)
#         for i in range(6):
#             n = ar[n]['compatibility'][0]
#             parts.append(n)
#         add_build_to_db([3], ['Good PC'], parts)

# addBuild()



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


add_user_to_db("doffy", '1', 'customer', 'd@mail.com', 'Doffy', 'last')
# add_user_to_db("alex", 'qwerty', 'admin', 'a@mail.com', 'Alexander', 'Rimerov')

# def add_part_to_db(part_id, part_type, compatibility, name, price):
#     body = {'part_id': part_id, "part_type": part_type, "compatibility": compatibility, "name": name, "price": price}
#     req_url = f'{api_route}/part/add'
#     r = requests.post(req_url, json=body)
#     r_json = r.json()
#     try:
#         data = r_json['info']
#     except:
#         data = r_json['error']
#     return data

# #case, motherboard, processor, GPU, RAM, Hard Drive, PSU

# # Cases
# add_part_to_db('001', 'case', ['101', '102', '103'], 'Cooler Master MasterBox Q300 Micro-ATX', 66.99)
# add_part_to_db('002', 'case', ['101', '102', '103'], 'Thermaltake Versa H17 Micro-ATX', 44.99)
# add_part_to_db('003', 'case', ['104', '105', '106'], 'Lian-Li Case O11D Mid-Tower', 199.00)
# add_part_to_db('004', 'case', ['101', '102', '103', '104', '105', '106'], 'Corsair 4000D Airflow Tempered Glass Mid-Tower', 94.99)
# add_part_to_db('005', 'case', ['104', '105'], 'GAMDIAS White RGB Gaming Mid-Tower', 59.99)
# add_part_to_db('006', 'case', ['101', '103', '106'], 'Corsair iCUE 4000X RGB Tempered Glass Mid-Tower', 129.99)

# # MOBO
# add_part_to_db('101', 'motherboard', ['201'], 'MSI MPG Z590 MoBo (10-11th Gen Intel)', 134.00)
# add_part_to_db('102', 'motherboard', ['201', '202', '203'], 'ASRock B365 MoBo (9th Gen Intel)', 106.97)
# add_part_to_db('103', 'motherboard', ['201', '202', '203'], 'ASRock Intel B365 (9th Gen Intel)', 69.99)
# add_part_to_db('104', 'motherboard', ['204', '205', '206'], 'ASUS Prime B550-PLUS MoBo (Ryzen 5)', 132.99)
# add_part_to_db('105', 'motherboard', ['207', '208'], 'MSI MAG B550 TOMAHAWK MoBo (Ryzen 7)', 169.99)
# add_part_to_db('106', 'motherboard', ['209', '210'], 'ASUS AM4 TUF Gaming X570-Plus MoBo (Ryzen 9)', 209.99)
# add_part_to_db('107', 'motherboard', ['210'], 'MSI PRo X670-P ProSeries MoBo (Ryzen 9 7600K)', 249.99)

# #CPU
# add_part_to_db('201', 'cpu', ['303'], 'Intel Core i3-9100F (9th Gen)', 120)
# add_part_to_db('202', 'cpu', ['301', '302', '303'], 'Intel Core i5-10400F (10th Gen)', 110.88)
# add_part_to_db('203', 'cpu', ['301', '302'], 'Intel Core i7-10700KF (10th Gen)', 241.11)
# add_part_to_db('204', 'cpu', ['301', '302'], 'Intel Core i9-11900L (11th Gen)', 300.54)
# add_part_to_db('205', 'cpu', ['305'], 'Ryzen 5 5500', 89.99)
# add_part_to_db('206', 'cpu', ['306'], 'Ryzen 5 5600', 136.44)
# add_part_to_db('207', 'cpu', ['307'], 'Ryzen 7 5700X', 192.99)
# add_part_to_db('208', 'cpu', ['304', '309'], 'Ryzen 7 5800X', 239.00)
# add_part_to_db('209', 'cpu', ['308'], 'Ryzen 9 5900X', 325.73)
# add_part_to_db('210', 'cpu', ['308', '309'], 'Ryzen 9 7900X', 416.33)

# #GPU
# add_part_to_db('301', 'gpu', ['401', '402', '403'], 'ASUS TUF NVIDIA RTX 3060', 379.99)
# add_part_to_db('302', 'gpu', ['401', '402', '403'], 'ASUS ROG Strix NVIDIA RTX 3060', 669.00)
# add_part_to_db('303', 'gpu', ['401', '403'], 'PNY GTX 1650', 184.76)
# add_part_to_db('304', 'gpu', ['404', '405', '406'], 'ASUS RTX 2060', 344.97)
# add_part_to_db('305', 'gpu', ['401', '402'], 'ASRock RX 570', 139.99)
# add_part_to_db('306', 'gpu', ['404', '406'], 'Gigabyte RX 580', 108.22)
# add_part_to_db('307', 'gpu', ['403'], 'PowerColor Fighter RX 6500 XT', 169.00)
# add_part_to_db('308', 'gpu', ['405', '406'], 'PowerColor Fighter RX 6600', 209.99)
# add_part_to_db('309', 'gpu', ['403', '405', '406'], 'PowerColor Fighter RX 6700 XT', 349.99)

# #RAM
# add_part_to_db('401', 'ram', ['501', '502', '503', '504', '505', '506', '507', '508', '509', '510', '511', '512', '513'], 'Corsair Vengeance LPX 16GB (2x8GB)', 39.99)
# add_part_to_db('402', 'ram', ['501', '502', '503', '504', '505', '506', '507', '508', '509', '510', '511', '512', '513'], 'TEAMGROUP T-Force Vulcan Z 16GB (2x8GB)', 34.99)
# add_part_to_db('403', 'ram', ['501', '502', '503', '504', '505', '506', '507', '508', '509', '510', '511', '512', '513'], 'Patriot Viper Steel 16GB (1x16GB)', 33.99)
# add_part_to_db('404', 'ram', ['504', '505', '506', '507', '508', '509', '510', '511', '512', '513'], 'Corsair Vengeance RGB Pro 32GB (2x16GB)', 79.99)
# add_part_to_db('405', 'ram', ['504', '505', '506', '507', '508', '509', '510', '511', '512', '513'], 'Corsair Vengeance LPX 32GB (2x16GB)', 69.99)
# add_part_to_db('406', 'ram', ['501', '502', '503', '504', '505', '506', '507', '508', '509', '510', '511', '512', '513'], 'TEAMGROUP T-Force Vulcan Z 32GB (2x16GB)', 59.99)

# #HD
# add_part_to_db('501', 'storage', ['601', '602', '603', '604', '605', '606'], 'Seagate BarraCuda 1TB HDD', 39.99)
# add_part_to_db('502', 'storage', ['601', '602', '603', '604', '605', '606'], 'Seagate BarraCuda 2TB HDD', 49.99)
# add_part_to_db('503', 'storage', ['601', '602', '603', '604', '605', '606'], 'Seagate BarraCuda 4TB HDD', 67.99)
# add_part_to_db('504', 'storage', ['601', '602', '603', '604', '605', '606'], 'TEAMGROUP MP33 512GB NVMe M.2 SSD', 26.49)
# add_part_to_db('505', 'storage', ['601', '602', '603', '604', '605', '606'], 'SAMSUNG 970 EVO Plus 1TB NVMe M.2 SSD', 59.99)
# add_part_to_db('506', 'storage', ['601', '602', '603', '604', '605', '606'], 'SAMSUNG 980 EVO 1TB NVMe M.2 SSD', 59.99)
# add_part_to_db('507', 'storage', ['601', '602', '603', '604', '605', '606'], 'Crucial P3 Plus 1TB NVMe M.2 SSD', 51.99)
# add_part_to_db('508', 'storage', ['601', '602', '603', '604', '605', '606'], 'SAMSUNG 980 EVO Pro 2TB NVMe M.2 SSD', 139.99)
# add_part_to_db('509', 'storage', ['601', '602', '603', '604', '605', '606'], 'SAMSUNG 970 EVO Plus 2TB NVMe M.2 SSD', 129.99)
# add_part_to_db('510', 'storage', ['601', '602', '603', '604', '605', '606'], 'WD_BLACK SN770 2TB NVMe M.2 SSD', 109.99)
# add_part_to_db('511', 'storage', ['601', '602', '603', '604', '605', '606'], 'Crucial P3 Plus 4TB NVMe M.2 SSD', 223.99)
# add_part_to_db('512', 'storage', ['601', '602', '603', '604', '605', '606'], 'WD_BLACK SN850X 4TB NVMe M.2 SSD', 393.77)
# add_part_to_db('513', 'storage', ['601', '602', '603', '604', '605', '606'], 'TEAMGROUP MP34 4TB NVMe SSD', 199.99)

# #PSU
# add_part_to_db('601', 'psu', [], 'Zalman GigaMax 600W 80+ Bronze PSU', 54.99)
# add_part_to_db('602', 'psu', [], 'ASUS TUF GAMING 550W Bronze PSU', 89.99)
# add_part_to_db('603', 'psu', [], 'Thermaltake Toughpower GX2 600W 80+ Gold PSU', 66.99)
# add_part_to_db('604', 'psu', [], 'Pystart 1000W 80+ Gold PSU', 119.99)
# add_part_to_db('605', 'psu', [], 'Segotep 750W 80+ Gold PSU', 89.99)
# add_part_to_db('606', 'psu', [], 'AGK ARESGAME 850W 80+ Gold PSU', 99.99)
