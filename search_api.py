from flask_restful import Resource, reqparse
from search_clients import GoogleClient, DdgoClient, Twitter_Client 

class SearchAPI(Resource):
    def get(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('q', type=str, location='args')
        query = parser.parse_args()
        requ= query.q
        search_str=query.q.replace(" ", "+")
        g = GoogleClient().search(search_str)
        d = DdgoClient().search(requ)
        t = Twitter_Client().search(search_str)
        return {
            "query": requ,
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
                }
            }