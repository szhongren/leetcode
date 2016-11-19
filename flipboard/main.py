import urllib.request as url_req
import urllib.response as url_res
import json

site = "https://challenge.flipboard.com"

f = url_req.urlopen(site)

data = json.loads(f.read().decode("utf-8"))
print(data)