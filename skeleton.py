import json
import random

json_file = open('2017.json')
json_str = json_file.read()
json_data = json.loads(json_str)


def getText(tweet):
	return tweet["text"]

# REPLACE THIS CODE
for tweet in json_data:
	print getText(tweet)


