
import requests

r = requests.get('http://apiv3.iucnredlist.org/api/v3/docs')
print (r.json())
