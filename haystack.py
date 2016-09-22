import urllib2

import json

data = {
    'token':'273f6f91f957b33d54932c58f3555c69'
    }

req = urllib2.Request('http://challenge.code2040.org/api/haystack')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))

var = response.read()
var = json.loads(var)
needle = var['needle']
haystack = var['haystack']
indx = haystack.index(needle)

data = {
    'token':'273f6f91f957b33d54932c58f3555c69',
    'needle':indx
    }

req = urllib2.Request('http://challenge.code2040.org/api/haystack/validate')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
