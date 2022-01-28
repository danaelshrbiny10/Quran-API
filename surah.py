from flask import Flask 
from flask_restful import Resource, Api
import requests


app = Flask(__name__)
api = Api(app)

surah_url = 'http://api.alquran.cloud/v1/surah'  # Get a Surah of the Quran 

while True:
    class Quran(Resource):

        def get(self):
            payload={}
            headers = {}

            response = requests.request("GET" ,surah_url ,headers=headers ,data=payload).json()
            print(response)
            

    break

api.add_resource(Quran, '/surah',methods=['GET'])
    


if __name__ == '__main__':
    app.run(debug=True)