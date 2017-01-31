import urllib
import simplejson

num_queries = 50*4 
query = urllib.urlencode({'q' : 'example'})
url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query

for start in range(0, num_queries, 4):
    request_url = '{0}&start={1}'.format(url, start)
    search_results = urllib.urlopen(request_url)
    json = simplejson.loads(search_results.read())
    results = json['responseData']['results']
    for i in results:
        print i['title'] + ": " + i['url']
