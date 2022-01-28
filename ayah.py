from flask import Flask 
from flask_restful import Resource, Api
import requests


app = Flask(__name__)
api = Api(app)


ayah_url = 'http://api.alquran.cloud/v1/ayah/262/editions/quran-uthmani,en.asad,en.pickthall%20-'  # Returns Ayat Al Kursi from 3 editions: Simple Quran, Muhammad Asad and Maramduke Pickthall

while True:
    class Ayah(Resource):

        def get(self):
            payload={}
            headers = {}

            response = requests.request("GET" ,ayah_url ,headers=headers ,data=payload).json()
            print(response)
            

    break

api.add_resource(Ayah, '/ayah',methods=['GET'])
    


if __name__ == '__main__':
    app.run(debug=True)