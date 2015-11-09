import requests
from requests_oauthlib import OAuth1
import sys
import urllib2

#set the API URL here:
url = sys.argv[sys.argv.index('-url')+1]
print url

if "-u" in sys.argv:
  user = sys.argv[sys.argv.index('-u')+1]
else:
  user = "none"

if "-p" in sys.argv:
  password = sys.argv[sys.argv.index('-p')+1]
else:
  password = "none"

if "--encrypted" in sys.argv:
  encrypted = "true"
else:
  encrypted = "false"

if "-k" in sys.argv:
  k_i = sys.argv.index('-k')+1
  key = sys.argv[k_i]
else:
  key = "none"

if (encrypted == "true"):
  if (user != "none"):
    resp = requests.get(url, auth=HTTPDigestAuth(user,password))
else:
  if (user != "none"):
    resp = requests.get(url, auth=(user,password))
  else:
    print "use key authentication"
    payload = {'apikey': key}
    resp = requests.get(url, data=payload)
if resp.status_code !=200:
  #this means something went wrong
  raise ApiError(url+ format(resp.status_code))
else:
  print resp.headers['content-type']
  print resp.json()
