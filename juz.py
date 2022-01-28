from flask import Flask 
from flask_restful import Resource, Api
import requests


app = Flask(__name__)
api = Api(app)


juz_url = 'http://api.alquran.cloud/v1/juz/30/en.asad%20-' # Get a Juz of the Quran

while True:
    class Juz(Resource):

        def get(self):
            payload={}
            headers = {}

            response = requests.request("GET" ,juz_url ,headers=headers ,data=payload).json()
            print(response)
            

    break

api.add_resource(Juz, '/juz',methods=['GET'])
    


if __name__ == '__main__':
    app.run(debug=True)