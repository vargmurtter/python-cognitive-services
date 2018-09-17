import requests
from pprint import pprint 

key = '<Key>'
url = 'https://westeurope.api.cognitive.microsoft.com/vision/v2.0/ocr'

print("Enter the path to image:", end=' ')
image_path = input()
print(end='\n')

image = open(image_path, "rb").read()

headers = {'Ocp-Apim-Subscription-Key': key, 'Content-Type': 'application/octet-stream'}
params = {'language': 'en', 'detectOrientation': 'true'}
response = requests.post(url, headers=headers, params=params, data=image)

json = response.json()
pprint(json)

for region in json['regions']:
	for line in region['lines']:
		print(end='\n')
		for word in line['words']:
			print(word['text'], end=' ')
print(end='\n')