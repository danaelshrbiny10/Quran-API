from flask import Flask 
from flask_restful import Resource, Api
import requests


app = Flask(__name__)
api = Api(app)

# Get adhan calendar By City
adhan_url = " https://api.aladhan.com/v1/calendarByCity?city=egypt&country=kaferelshiekh&method=1&month=01&year=2022"  

while True:
    class Adhan(Resource):

        def get(self):
            payload={}
            headers = {}

            response = requests.request("GET" ,adhan_url ,headers=headers ,data=payload).json()
            print(response)
            

    break

api.add_resource(Adhan, '/adhan',methods=['GET'])
    


if __name__ == '__main__':
    app.run(debug=True)