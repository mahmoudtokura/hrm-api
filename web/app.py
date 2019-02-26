from flask import Flask
from flask_restful import Api
from resources.employees import Employees
from ma import ma
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)


api.add_resource(Employees, '/')


if __name__ == '__main__':
    ma.init_app(app)
    app.run(debug=True, host='0.0.0.0')
