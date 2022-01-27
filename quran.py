from flask import Flask ,jsonify
from flask_restful import Resource, Api
import requests
import json


app = Flask(__name__)
api = Api(app)

quran_url = "https://quran.com/"

while True:
    class Quran(Resource):

        def get(self):
            payload={}
            headers = {
            'Cookie': '_quran_session=RazYbVYFJeEa0%2Fp1%2BEEy9onXnjf9C%2FgSf0cI2Iaoj7wMjvQ%2FRak9kAVb1kvlqmSwKCIeTW7miQhEVG54HV2W5NUWHFu6220Sxsk4ff5SaTgJTNkB2cgOSf6XfdLy%2BBnLKKBKCEhDUmIVG0FBRSp4YKc9mj0FuY4syXuskYx9nwXZ%2FHa%2BLkh38rMChBOY131meWz6xNYGLIFnjSabOGtpDQUeErH35dj4PLjqduRyqi%2FP9hjAzcs%3D--GuDSFXv3X6uabXVE--mvrSCmWvxbJJf2qI6WnVYQ%3D%3D'
            }

            response = requests.request("GET", quran_url, headers=headers, data=payload).json()
            # response = str(json.loads(requests.request("GET", quran_url, headers=headers, data=payload)))
            # result = str(response)
            return jsonify({
                response
            })
        if quran_url == "https://quran.com/115":
            print ("page not found")
    break

api.add_resource(Quran, '/',methods=['GET'])
    


if __name__ == '__main__':
    app.run(debug=True)