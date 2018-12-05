import requests
import time
# If you are using a Jupyter notebook, uncomment the following line.
# %matplotlib inline
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from PIL import Image
from io import BytesIO
import pylab
from skimage import io

def recognizeText(base_url,subscription_key,data_int):
	# Replace <Subscription Key> with your valid subscription key.
	#subscription_key = "<Subscription Key>"
	assert subscription_key

	# You must use the same region in your REST call as you used to get your
	# subscription keys. For example, if you got your subscription keys from
	# westus, replace "westcentralus" in the URI below with "westus".
	#
	# Free trial subscription keys are generated in the "westus" region.
	# If you use a free trial subscription key, you shouldn't need to change
	# this region.
	#base_url = 'westcentralus.api.cognitive.microsoft.com'
	vision_base_url = "https://" + base_url + "/vision/v2.0/"

	text_recognition_url = vision_base_url + "recognizeText"

	if type(data_int)==type(''):
		headers = {'Ocp-Apim-Subscription-Key': subscription_key}
		# Note: The request parameter changed for APIv2.
		# For APIv1, it is 'handwriting': 'true'.
		params = {'mode': 'Handwritten'}
		data = {'url': data_int}
		response = requests.post(
			text_recognition_url, headers=headers, params=params, json=data)
	else:
		headers = {'Ocp-Apim-Subscription-Key': subscription_key,\
				   'Content-Type': 'application/octet-stream'}
		# Note: The request parameter changed for APIv2.
		# For APIv1, it is 'handwriting': 'true'.
		params = {'mode': 'Handwritten'}
		response = requests.post(
			text_recognition_url, headers=headers, params=params, data=data_int)


	response.raise_for_status()

	# Extracting handwritten text requires two API calls: One call to submit the
	# image for processing, the other to retrieve the text found in the image.

	# Holds the URI used to retrieve the recognized text.
	operation_url = response.headers["Operation-Location"]

	# The recognized text isn't immediately available, so poll to wait for completion.
	analysis = {}
	poll = True
	while (poll):
		response_final = requests.get(
			response.headers["Operation-Location"], headers=headers)
		analysis = response_final.json()
		time.sleep(1)
		if ("recognitionResult" in analysis):
			poll = False
		if ("status" in analysis and analysis['status'] == 'Failed'):
			poll = False

	polygons = []
	def avg_point(li):
		avg=[0,0]
		for i in range(len(li)):
			avg[i%2]+=li[i]
		return avg[0]*2/i+avg[1]*2/i*1000000

	if ("recognitionResult" in analysis):
		# Extract the recognized text, with bounding boxes.
		polygons = [[avg_point(line["boundingBox"]),line["text"]]
			for line in analysis["recognitionResult"]["lines"]]
	polygons.sort(key=lambda x:x[0])
	polygons=[ x[1] for x in polygons]

	'''
	print(analysis)
	polygons = []
	if ("recognitionResult" in analysis):
		# Extract the recognized text, with bounding boxes.
		polygons = [(line["boundingBox"], line["text"])
			for line in analysis["recognitionResult"]["lines"]]
	
	# Display the image and overlay it with the extracted text.
	plt.figure(figsize=(15, 15))
	image = Image.open(BytesIO(requests.get(image_url).content))
	ax = plt.imshow(image)
	# pylab.show()
	for polygon in polygons:
		vertices = [(polygon[0][i], polygon[0][i + 1])
			for i in range(0, len(polygon[0]), 2)]
		text = polygon[1]
		patch = Polygon(vertices, closed=True, fill=False, linewidth=2, color='y')
		ax.axes.add_patch(patch)
		plt.text(vertices[0][0], vertices[0][1], text, fontsize=20, va="top")
	print(type(ax), dir(ax))
	pylab.show()
	# io.show()
	_ = plt.axis("off")
	'''
	return polygons,analysis


if __name__=='__main__':
	import json
	fo = open("conf.ini", "r")
	cof=json.load(fo)
	fo.close()

	li,_=recognizeText(cof['base_url'],cof['subscription_key'],\
		"https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/" + \
		"Cursive_Writing_on_Notebook_paper.jpg/800px-Cursive_Writing_on_Notebook_paper.jpg"	)
	for item in li:
		print(item)

	img = open("E:/Users/Desktop/Atom/Edit.png", "rb")
	img_data=img.read()
	li,_=recognizeText(cof['base_url'],cof['subscription_key'],img_data	)
	img.close()
	for item in li:
		print(item)
