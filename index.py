from flask import Flask, request
from flask_restful import Resource, Api
from nsetools import Nse
from flask_cors import CORS, cross_origin
# from pprint import pprint

app = Flask(__name__)
api = Api(app)

CORS(app)

nse = Nse()

@app.route('/')
def quote():
    return "Hello!"

class NseData(Resource):
    def get(self, quote):
        return nse.get_index_quote(quote)

api.add_resource(NseData, '/nsedata/<quote>')


# pprint(nse.get_index_quote("nifty 50"))
if __name__ == "__main__":
    app.run(port=5002)