import json
import urllib2

data = {
    'token':'273f6f91f957b33d54932c58f3555c69',
    'github':'https://github.com/WilliamDBell/CODE2040CHALLENGE'
}

req = urllib2.Request('http://challenge.code2040.org/api/register')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))

