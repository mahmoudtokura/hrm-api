from schemas.department import DepartmentSchema
from db import db
from flask_restful import Resource
from flask import request

department_collection = db['department']
department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many=True)


class Department(Resource):
    def post(self):
        department_json = request.get_json()

        if department_json['HOD'] is None or department_json['HOD'] is "":
            department_json['HOD'] = "Unassigned"
        department_collection.insert(department_json)
        return department_schema.dump(department_json), 200

    def get(self):
        all_departments = department_collection.find({})
        return departments_schema.dump(all_departments), 200


class Departments(Resource):
    def get(self):
        all_departments = department_collection.find({})
        return departments_schema.dump(all_departments), 200


