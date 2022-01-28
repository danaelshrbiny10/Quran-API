from flask import Flask 
from flask_restful import Resource, Api
import requests


app = Flask(__name__)
api = Api(app)

edition_url = 'http://api.alquran.cloud/v1/edition'  # Lists all available editions. 

while True:
    class Holy(Resource):

        def get(self):
            payload={}
            headers = {}

            response = requests.request("GET" ,edition_url ,headers=headers ,data=payload).json()
            print(response)
            

    break

api.add_resource(Holy, '/',methods=['GET'])
    


if __name__ == '__main__':
    app.run(debug=True)