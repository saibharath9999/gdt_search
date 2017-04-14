from flask import Flask
from flask_restful import Api
from search_api import SearchAPI

app = Flask(__name__)
api = Api(app)

api.add_resource(SearchAPI, '/', endpoint='')

if __name__ == '__main__':
    app.run(debug=True)
