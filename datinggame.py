import json
import urllib2
import datetime
from dateutil.parser import parse


data = {
    'token':'273f6f91f957b33d54932c58f3555c69',
}

req = urllib2.Request('http://challenge.code2040.org/api/dating')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))

var = response.read()
var = json.loads(var)

initialDate = var['datestamp']
duration = var['interval']
print initialDate
print duration

# Parse initial datestamp string
parsedInitialDate = parse(initialDate)

# Create Time difference object
delta = datetime.timedelta(seconds = int(duration))

# Add delta to initial timestamp
newDate = parsedInitialDate + delta

# Format newdate
newDate = newDate.isoformat()[:19] + 'Z'
print newDate

data = {
    'token':'273f6f91f957b33d54932c58f3555c69',
    'datestamp':newDate
}


req = urllib2.Request('http://challenge.code2040.org/api/dating/validate')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
