
import requests     #will import the module called requests

r = requests.get('http://www.reddit.com/api/info') # will request for data from the reddit 
print (r.json())    # Will give the final output
