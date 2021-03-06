from flask import Flask 
from flask_restful import Resource, Api
import requests


app = Flask(__name__)
api = Api(app)

quran_url = " http://api.alquran.cloud/v1/quran/ar.alafasy -"  # Get a complete Quran edition

while True:
    class Quran(Resource):

        def get(self):
            payload={}
            headers = {}

            response = requests.request("GET" ,quran_url ,headers=headers ,data=payload).json()
            print(response)
            

    break

api.add_resource(Quran, '/quran',methods=['GET'])
    


if __name__ == '__main__':
    app.run(debug=True)