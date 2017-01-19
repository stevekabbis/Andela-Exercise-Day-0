import requests     #will import the module called requests

r = requests.get('http://www.reddit.com/r/history') # will request for data from the subreddit called history
print (r.json())    # Will give the final output

