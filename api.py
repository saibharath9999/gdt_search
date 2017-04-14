from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from SearchClients import googl, ddgo, tweet 



app = Flask(__name__)
api = Api(app)


class SearchAPI(Resource):
    def get(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('q', type=str, location='args')
        query = parser.parse_args()
        requ= query.q
        search_str=query.q.replace(" ", "+")
        g = googl(search_str)
        d = ddgo(requ)
        t = tweet(search_str)
        result= {"query": requ,
"results": {
"google": {
"url": "https://"+g[1]+"",
"text": g[0]
},
"twitter": {
"url": t[0],
"text": t[1]
},
"duckduckgo": {
"url": d[0],
"text": d[1]
}
}}
        return result



api.add_resource(SearchAPI, '/', endpoint='')

if __name__ == '__main__':
    app.run(debug=True)