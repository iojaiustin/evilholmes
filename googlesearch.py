from googleapiclient.discovery import build
import pprint
import yaml

with open('config/evilholmes.yml') as stream:
    config = yaml.safe_load(stream)


my_api_key = config['GOOGLE-API-KEY']
my_cse_id = config['CSE-ID']

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def search(keyword,domain):
    urls = []
    query = 'site:'+domain+' intext:"' + keyword + '"'
    results = google_search(keyword, my_api_key, my_cse_id, num=10)
    for result in results:
        if domain in result['link']:
            urls.append(result['link'])

    return urls
