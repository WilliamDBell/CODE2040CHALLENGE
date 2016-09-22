import urllib2

import json

data = {
    'token':'273f6f91f957b33d54932c58f3555c69'
    }

req = urllib2.Request('http://challenge.code2040.org/api/prefix')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))

var = response.read()
var = json.loads(var)
prefix = var['prefix']
array = var['array']

array = [x for x in array if x[0:len(prefix)] != prefix]

data = {
    'token':'273f6f91f957b33d54932c58f3555c69',
    'array':array
    }

 req = urllib2.Request('http://challenge.code2040.org/api/prefix/validate')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
