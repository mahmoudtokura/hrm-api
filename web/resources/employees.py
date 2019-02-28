import uuid
from flask import request
from flask_restful import Resource
from db import db
from schemas.employee import EmployeeSchema

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)


class Employee(Resource):
    def post(self):
        employees = db['employees']
        employee_id = uuid.uuid4().hex
        employee_json = request.get_json()
        employee_json['employee_id'] = employee_id
        employee = employee_schema.load(employee_json)
        employees.insert(employee)
        return employee_schema.dump(employee), 200


class Employees(Resource):
    def get(self):
        employees = db['employees']

        employee_list = employees.find({})
        return employees_schema.dump(employee_list), 200
