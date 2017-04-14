import urllib
import urllib2
import json
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

def googl(search):
    #getting the results from google API
    google = "https://www.googleapis.com/customsearch/v1?key=AIzaSyA2r3oK7Fxr8GiKKsE9D7hGxoJRtdQCnKo&cx=014170932909531414778:kcyx0xaz-60&q="+search+""
    request = urllib2.Request(google)
    response = urllib2.urlopen(request)
    data = json.loads(response.read())
    items= data.get('items')
    item= items[0]
    google_detail= item.get('snippet')
    google_url= item.get('formattedUrl')
    return [google_detail, google_url]

def ddgo(search):
    ddg = "https://api.duckduckgo.com/?q="+search+"&format=json"
    ddg_request = urllib2.Request(ddg)
    ddg_response = urllib2.urlopen(ddg_request)
    ddg_data = json.loads(ddg_response.read())
    ddg_items= ddg_data.get('RelatedTopics')
    try:
        ddg_item= ddg_items[0]
    except (IndexError, ValueError):
        ddg_item = "null"
    if ddg_item!="null":
        ddg_detail=ddg_item.get("Text")
        ddg_url=ddg_item.get("FirstURL")
    else :
        ddg_detail="No response from search engine"
        ddg_url="No response from search engine"
    return [ddg_url,ddg_detail]

def tweet(search):
    #generating results from twitter
    # Variables that contains the user credentials to access Twitter API 
    ACCESS_TOKEN = '2246017367-k0H9mvIMnUXCCfnKD2CQXE8pGSlmBnwSkPHede7'
    ACCESS_SECRET = 'LS6xNwiF8nKuvwNxTslPNUeVXA90JZD3vwHUxfsXL8S9z'
    CONSUMER_KEY = 'EOXNXZXfnSjRP0Mo254KZfhVi'
    CONSUMER_SECRET = 'TUCdpFQXqIqFq9dX8e9PsSBJUM7rzWsoCINVWywRJVdBzreJOx'
    oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter = Twitter(auth=oauth)
    t_data=twitter.search.tweets(q=search, result_type='recent', lang='en', count=10)
    t_detail= t_data['statuses'][0]['text']
    try:
        t_url = t_data['statuses'][0]['entities']['urls'][0]['url']
    except (IndexError, ValueError):
    	t_url = "No response from search engine"
    return [t_url,t_detail]