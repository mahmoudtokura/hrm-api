import uuid

from flask_restful import Resource
from db import db
from schemas.users import EmployeeSchema

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)


class Employees(Resource):
    def get(self):
        employees = db['employees']
        # employee_id = uuid.uuid4().hex
        # employees.insert(
        #     {
        #         "employee_id": employee_id,
        #         "name": "Leanne Graham",
        #         "username": "Bret",
        #         "email": "Sincere@april.biz",
        #         "image": "https://cdn.vuetifyjs.com/images/lists/ali.png",
        #         "address": {
        #             "street": "Kulas Light",
        #             "suite": "Apt. 556",
        #             "city": "Gwenborough",
        #             "zipcode": "92998-3874"
        #                     },
        #         "phone": "1-770-736-8031 x56442",
        #         "department": "Admin",
        #         "designation": "HOD",
        #         "pay": {
        #         "salary": 400000,
        #         "deduction": {
        #         "health_insurance": 25000,
        #         "loan": 0
        #                     }
        #
        #             },
        #         "leave": {
        #   'total': 25,
        #   'taken': [
        #     {
        #       'date': "20th June 2018",
        #       'days': 5,
        #       'reason': "Sick leave"
        #     },
        #     {
        #       'date': "10th Jan 2019",
        #       'days': 5,
        #       'reason': "Sick leave"
        #     }
        #   ]
        # }
        #     }
        #
        # )
        employee_list = employees.find({})
        print(type(employee_list))
        return {'message': employees_schema.dump(employee_list)}
