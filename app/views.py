from flask import request

from app import app
from app.models import object, package
from app import ma
import json

@app.route('/get_object/<int:object_id>', methods=['GET'])
def get_object_by_id(object_id):
    data = dict()
    Object = object.get_by_id(object_id)
    data['Object_ID'] = Object[0][0]
    data['Stereotype'] = Object[0][1]
    data['Name'] = Object[0][2]
    data['PDATA1'] = Object[0][3]
    return data

@app.route('/get_object/<string:ea_guid>', methods=['GET'])
def get_object_by_ea_guid(ea_guid):
    data = dict()
    Object = object.get_by_ea_guid(ea_guid)
    data['Object_ID'] = Object[0][0]
    data['Stereotype'] = Object[0][1]
    data['Name'] = Object[0][2]
    data['PDATA1'] = Object[0][3]
    return data

@app.route('/add_object', methods=['POST'])
def add_object():
    name = request.json.get('Name')
    stereotype = request.json.get('Stereotype')
    object_type = request.json.get('Object_Type')
    package_id = request.json.get('Package_ID')
    parent_id = request.json.get('Parent_ID')
    object.add_object(name, stereotype, object_type, package_id, parent_id)
    return "OK"

@app.route('/update_object/<int:object_id>', methods=['PUT'])
def update_object(object_id):
    name = request.json.get('Name')
    stereotype = request.json.get('Stereotype')
    object.update_object(name, stereotype, object_id)
    return get_object_by_id(object_id)


@app.route('/delete_object/<string:ea_guid>', methods=['DELETE'])
def delete_object(ea_guid):
    result = get_object_by_ea_guid(ea_guid)
    object.delete_by_ea_guid(ea_guid)
    return result

@app.route('/add_package', methods=['POST'])
def add_package():
    name = request.json.get('Name')
    notes = request.json.get('Notes')
    stereotype = request.json.get('Stereotype')
    object_type = request.json.get('Object_Type')
    parent_id = request.json.get('Parent_ID')
    package.add_package(name, notes, stereotype, object_type, parent_id)
    return "OK"

@app.route('/get_package/<int:package_id>', methods=['GET'])
def get_package(package_id):
    pack = package.get_by_id(package_id)
    data = dict()
    data['Package_ID'] = pack[0][0]
    data['Name'] = pack[0][1]
    data['Notes'] = pack[0][2]
    return data

@app.route('/get_package/<int:ea_guid>', methods=['GET'])
def get_package_by_ea_guid(ea_guid):
    pack = package.get_by_ea_guid(ea_guid)
    data = dict()
    data['Package_ID'] = pack[0][0]
    data['Name'] = pack[0][1]
    data['Notes'] = pack[0][2]
    return data

@app.route('/update_package/<int:package_id>', methods=['PUT'])
def update_package(package_id):
    name = request.json.get('Name')
    notes = request.json.get('Notes')
    stereotype = request.json.get('Stereotype')
    package.update_package(name, notes, stereotype, package_id)
    return get_package(package_id)

@app.route('/delete_package/<string:ea_guid>', methods=['DELETE'])
def delete_package(ea_guid):
    result = get_package_by_ea_guid(ea_guid)
    package.delete_by_ea_guid(ea_guid)
    return result

