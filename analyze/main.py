import requests
from pprint import pprint 

key = '<Key>'
url = 'https://westeurope.api.cognitive.microsoft.com/vision/v2.0/analyze'

print("Enter the path to image:", end=' ')
image_path = input()
print(end='\n')

image = open(image_path, "rb").read()

headers = {'Ocp-Apim-Subscription-Key': key, 'Content-Type': 'application/octet-stream'}
params = {'visualFeatures': 'Categories,Description,Faces'}
response = requests.post(url, headers=headers, params=params, data=image)

json = response.json()
pprint(json)

print('Tags: {0}'.format(', '.join(json['description']['tags'])), end='\n\n')

if len(json['description']['captions']) != 0:
	print('Description: {0}'.format(json['description']['captions'][0]['text']), end='\n\n')

if len(json['faces']) != 0:
	print('Age: {0}'.format(json['faces'][0]['age']), end='\n\n')
	print('Gender: {0}'.format(json['faces'][0]['gender']), end='\n\n')

