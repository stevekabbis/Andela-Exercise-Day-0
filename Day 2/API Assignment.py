
import requests

r = requests.get('http://www.reddit.com/r/history')
print (r.json())
