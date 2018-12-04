# -*- conding: utf-8 -*-

import http.client, urllib.request, urllib.parse, urllib.error, base64
import re
import json

fo = open("conf.ini", "r")
cof = json.load(fo)
fo.close()

# Replace <Subscription Key> with your valid subscription key.
subscription_key = cof['subscription_key']
assert subscription_key
base_url = cof['base_url']
'''
version_url = '/vision/v1.0/' + 'recognizeText'
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}
params = urllib.parse.urlencode({
    # Request parameters
    'handwriting': 'false',
})
request_content='{"url":"https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=3691210852,3211033389&fm=58&bpow=533&bpoh=456"}'
'''
'''
version_url = '/vision/v1.0/' + 'recognizeText'
headers = {
	# Request headers
	'Content-Type': 'application/octet-stream',
	'Ocp-Apim-Subscription-Key': subscription_key,
}
params = urllib.parse.urlencode({
	# Request parameters
	'handwriting': 'false',
})
'''
version_url = '/vision/v1.0/' + 'ocr'
headers = {
	# Request headers
	'Content-Type': 'application/octet-stream',
	'Ocp-Apim-Subscription-Key': subscription_key,
}
params = urllib.parse.urlencode({
	# Request parameters
	'language': 'unk',
	'detectOrientation ': 'false',
})

image_path = "E:/Users/Desktop/Atom/Edit.png"
image_data = open(image_path, "rb").read()
request_content = image_data

try:
	'''
	conn = http.client.HTTPSConnection(base_url)
	conn.request("POST", version_url+"?%s" % params, request_content, headers)
	response = conn.getresponse()
	data = response.read()
	print(data)
	conn.close()
	'''

	# {"boundingBox":"183,3,32,10","text":"Packa"}
	pattern = '\{"boundingBox":\s*"(\d+),(\d+),(\d+),(\d+)",\s*"text":\s*"([^"]+)"\}'
	#json_str = data
	#json_str = '{"language":"en","textAngle":0.0,"orientation":"Up","regions":[{"boundingBox":"7,3,61,119","lines":[{"boundingBox":"7,3,61,10","words":[{"boundingBox":"7,3,21,10","text":"Edit"},{"boundingBox":"40,3,28,10","text":"View"}]},{"boundingBox":"28,26,30,10","words":[{"boundingBox":"28,26,30,10","text":"Undo"}]},{"boundingBox":"28,50,29,10","words":[{"boundingBox":"28,50,29,10","text":"Redo"}]},{"boundingBox":"27,110,30,12","words":[{"boundingBox":"27,110,15,9","text":"Co"},{"boundingBox":"44,113,13,9","text":"py"}]}]},{"boundingBox":"80,3,52,10","lines":[{"boundingBox":"80,3,52,10","words":[{"boundingBox":"80,3,52,10","text":"Selection"}]}]},{"boundingBox":"146,3,23,10","lines":[{"boundingBox":"146,3,23,10","words":[{"boundingBox":"146,3,23,10","text":"Find"}]}]},{"boundingBox":"183,3,32,10","lines":[{"boundingBox":"183,3,32,10","words":[{"boundingBox":"183,3,32,10","text":"Packa"}]}]},{"boundingBox":"223,3,49,116","lines":[{"boundingBox":"223,3,43,10","words":[{"boundingBox":"223,7,12,6","text":"es"},{"boundingBox":"249,3,17,10","text":"Hel"}]},{"boundingBox":"235,26,37,10","words":[{"boundingBox":"235,26,37,10","text":"Ctrl+Z"}]},{"boundingBox":"235,50,37,10","words":[{"boundingBox":"235,50,37,10","text":"Ctrl+V"}]},{"boundingBox":"235,85,37,10","words":[{"boundingBox":"235,85,37,10","text":"Ctrl+X"}]},{"boundingBox":"234,109,37,10","words":[{"boundingBox":"234,109,37,10","text":"Ctrl+C"}]}]},{"boundingBox":"27,133,160,333","lines":[{"boundingBox":"27,133,59,13","words":[{"boundingBox":"27,134,30,12","text":"Copy"},{"boundingBox":"61,133,25,10","text":"Path"}]},{"boundingBox":"28,158,30,9","words":[{"boundingBox":"28,158,6,9","text":"P"},{"boundingBox":"35,159,23,8","text":"aste"}]},{"boundingBox":"28,181,159,13","words":[{"boundingBox":"28,182,30,9","text":"Paste"},{"boundingBox":"61,181,47,10","text":"Without"},{"boundingBox":"113,181,74,13","text":"Reformatting"}]},{"boundingBox":"27,205,52,10","words":[{"boundingBox":"27,205,34,10","text":"Select"},{"boundingBox":"65,205,14,10","text":"All"}]},{"boundingBox":"27,240,106,13","words":[{"boundingBox":"27,240,40,13","text":"Toggle"},{"boundingBox":"71,241,62,9","text":"Comments"}]},{"boundingBox":"28,264,28,10","words":[{"boundingBox":"28,264,28,10","text":"Lines"}]},{"boundingBox":"27,289,50,9","words":[{"boundingBox":"27,289,15,9","text":"Co"},{"boundingBox":"46,292,31,6","text":"umns"}]},{"boundingBox":"28,336,41,13","words":[{"boundingBox":"28,336,41,13","text":"Folding"}]},{"boundingBox":"28,360,94,10","words":[{"boundingBox":"28,360,38,10","text":"Reflow"},{"boundingBox":"70,360,52,10","text":"Selection"}]},{"boundingBox":"28,384,58,10","words":[{"boundingBox":"28,384,58,10","text":"Bookmark"}]},{"boundingBox":"27,408,91,13","words":[{"boundingBox":"27,408,34,10","text":"Select"},{"boundingBox":"66,408,52,13","text":"Encoding"}]},{"boundingBox":"27,432,59,10","words":[{"boundingBox":"27,433,16,9","text":"Go"},{"boundingBox":"47,434,12,8","text":"to"},{"boundingBox":"64,432,22,10","text":"Line"}]},{"boundingBox":"27,456,92,10","words":[{"boundingBox":"27,456,34,10","text":"Select"},{"boundingBox":"65,457,54,9","text":"Grammar"}]}]},{"boundingBox":"198,133,74,333","lines":[{"boundingBox":"199,133,72,10","words":[{"boundingBox":"199,133,19,10","text":"Ctrl"},{"boundingBox":"221,136,6,7","text":"+"},{"boundingBox":"229,133,25,10","text":"Shift"},{"boundingBox":"256,136,6,7","text":"+"},{"boundingBox":"264,134,7,9","text":"C"}]},{"boundingBox":"234,157,37,10","words":[{"boundingBox":"234,157,37,10","text":"Ctrl+V"}]},{"boundingBox":"199,181,72,10","words":[{"boundingBox":"199,181,19,10","text":"Ctrl"},{"boundingBox":"221,184,6,7","text":"+"},{"boundingBox":"229,181,25,10","text":"Shift"},{"boundingBox":"256,184,6,7","text":"+"},{"boundingBox":"263,182,8,9","text":"V"}]},{"boundingBox":"234,205,38,10","words":[{"boundingBox":"234,205,19,10","text":"Ctrl"},{"boundingBox":"256,208,6,7","text":"+"},{"boundingBox":"263,206,9,9","text":"A"}]},{"boundingBox":"237,240,35,12","words":[{"boundingBox":"237,240,19,10","text":"Ctrl"},{"boundingBox":"259,243,6,7","text":"+"},{"boundingBox":"266,241,6,11","text":"/"}]},{"boundingBox":"198,360,74,11","words":[{"boundingBox":"198,360,19,10","text":"Ctrl"},{"boundingBox":"220,363,6,7","text":"+"},{"boundingBox":"228,360,25,10","text":"Shift"},{"boundingBox":"255,363,6,7","text":"+"},{"boundingBox":"263,361,9,10","text":"Q"}]},{"boundingBox":"198,408,72,10","words":[{"boundingBox":"198,408,19,10","text":"Ctrl"},{"boundingBox":"220,411,6,7","text":"+"},{"boundingBox":"228,408,25,10","text":"Shift"},{"boundingBox":"255,411,6,7","text":"+"},{"boundingBox":"263,409,7,9","text":"U"}]},{"boundingBox":"233,432,38,10","words":[{"boundingBox":"233,432,38,10","text":"Ctrl+G"}]},{"boundingBox":"201,456,71,10","words":[{"boundingBox":"201,456,19,10","text":"Ctrl"},{"boundingBox":"223,459,6,7","text":"+"},{"boundingBox":"231,456,25,10","text":"Shift"},{"boundingBox":"258,459,6,7","text":"+"},{"boundingBox":"266,457,6,9","text":"L"}]}]}]}'
	json_str = '{"language":"en","textAngle":0.0,"orientation":"Up","regions":[{"boundingBox":"7,3,61,119","lines":[{"boundingBox":"7,3,61,10","words":[{"boundingBox":"7,3,21,10","text":"Edit"},{"boundingBox":"40,3,28,10","text":"View"}]},{"boundingBox":"28,26,30,10","words":[{"boundingBox":"28,26,30,10","text":"Undo"}]},{"boundingBox":"28,50,29,10","words":[{"boundingBox":"28,50,29,10","text":"Redo"}]},{"boundingBox":"27,110,30,12","words":[{"boundingBox":"27,110,15,9","text":"Co"},{"boundingBox":"44,113,13,9","text":"py"}]}]},{"boundingBox":"80,3,52,10","lines":[{"boundingBox":"80,3,52,10","words":[{"boundingBox":"80,3,52,10","text":"Selection"}]}]},{"boundingBox":"146,3,23,10","lines":[{"boundingBox":"146,3,23,10","words":[{"boundingBox":"146,3,23,10","text":"Find"}]}]},{"boundingBox":"183,3,32,10","lines":[{"boundingBox":"183,3,32,10","words":[{"boundingBox":"183,3,32,10","text":"Packa"}]}]},{"boundingBox":"223,3,49,116","lines":[{"boundingBox":"223,3,43,10","words":[{"boundingBox":"223,7,12,6","text":"es"},{"boundingBox":"249,3,17,10","text":"Hel"}]},{"boundingBox":"235,26,37,10","words":[{"boundingBox":"235,26,37,10","text":"Ctrl+Z"}]},{"boundingBox":"235,50,37,10","words":[{"boundingBox":"235,50,37,10","text":"Ctrl+V"}]},{"boundingBox":"235,85,37,10","words":[{"boundingBox":"235,85,37,10","text":"Ctrl+X"}]},{"boundingBox":"234,109,37,10","words":[{"boundingBox":"234,109,37,10","text":"Ctrl+C"}]}]},{"boundingBox":"27,133,160,333","lines":[{"boundingBox":"27,133,59,13","words":[{"boundingBox":"27,134,30,12","text":"Copy"},{"boundingBox":"61,133,25,10","text":"Path"}]},{"boundingBox":"28,158,30,9","words":[{"boundingBox":"28,158,6,9","text":"P"},{"boundingBox":"35,159,23,8","text":"aste"}]},{"boundingBox":"28,181,159,13","words":[{"boundingBox":"28,182,30,9","text":"Paste"},{"boundingBox":"61,181,47,10","text":"Without"},{"boundingBox":"113,181,74,13","text":"Reformatting"}]},{"boundingBox":"27,205,52,10","words":[{"boundingBox":"27,205,34,10","text":"Select"},{"boundingBox":"65,205,14,10","text":"All"}]},{"boundingBox":"27,240,106,13","words":[{"boundingBox":"27,240,40,13","text":"Toggle"},{"boundingBox":"71,241,62,9","text":"Comments"}]},{"boundingBox":"28,264,28,10","words":[{"boundingBox":"28,264,28,10","text":"Lines"}]},{"boundingBox":"27,289,50,9","words":[{"boundingBox":"27,289,15,9","text":"Co"},{"boundingBox":"46,292,31,6","text":"umns"}]},{"boundingBox":"28,336,41,13","words":[{"boundingBox":"28,336,41,13","text":"Folding"}]},{"boundingBox":"28,360,94,10","words":[{"boundingBox":"28,360,38,10","text":"Reflow"},{"boundingBox":"70,360,52,10","text":"Selection"}]},{"boundingBox":"28,384,58,10","words":[{"boundingBox":"28,384,58,10","text":"Bookmark"}]},{"boundingBox":"27,408,91,13","words":[{"boundingBox":"27,408,34,10","text":"Select"},{"boundingBox":"66,408,52,13","text":"Encoding"}]},{"boundingBox":"27,432,59,10","words":[{"boundingBox":"27,433,16,9","text":"Go"},{"boundingBox":"47,434,12,8","text":"to"},{"boundingBox":"64,432,22,10","text":"Line"}]},{"boundingBox":"27,456,92,10","words":[{"boundingBox":"27,456,34,10","text":"Select"},{"boundingBox":"65,457,54,9","text":"Grammar"}]}]},{"boundingBox":"198,133,74,333","lines":[{"boundingBox":"199,133,72,10","words":[{"boundingBox":"199,133,19,10","text":"Ctrl"},{"boundingBox":"221,136,6,7","text":"+"},{"boundingBox":"229,133,25,10","text":"Shift"},{"boundingBox":"256,136,6,7","text":"+"},{"boundingBox":"264,134,7,9","text":"C"}]},{"boundingBox":"234,157,37,10","words":[{"boundingBox":"234,157,37,10","text":"Ctrl+V"}]},{"boundingBox":"199,181,72,10","words":[{"boundingBox":"199,181,19,10","text":"Ctrl"},{"boundingBox":"221,184,6,7","text":"+"},{"boundingBox":"229,181,25,10","text":"Shift"},{"boundingBox":"256,184,6,7","text":"+"},{"boundingBox":"263,182,8,9","text":"V"}]},{"boundingBox":"234,205,38,10","words":[{"boundingBox":"234,205,19,10","text":"Ctrl"},{"boundingBox":"256,208,6,7","text":"+"},{"boundingBox":"263,206,9,9","text":"A"}]},{"boundingBox":"237,240,35,12","words":[{"boundingBox":"237,240,19,10","text":"Ctrl"},{"boundingBox":"259,243,6,7","text":"+"},{"boundingBox":"266,241,6,11","text":"/"}]},{"boundingBox":"198,360,74,11","words":[{"boundingBox":"198,360,19,10","text":"Ctrl"},{"boundingBox":"220,363,6,7","text":"+"},{"boundingBox":"228,360,25,10","text":"Shift"},{"boundingBox":"255,363,6,7","text":"+"},{"boundingBox":"263,361,9,10","text":"Q"}]},{"boundingBox":"198,408,72,10","words":[{"boundingBox":"198,408,19,10","text":"Ctrl"},{"boundingBox":"220,411,6,7","text":"+"},{"boundingBox":"228,408,25,10","text":"Shift"},{"boundingBox":"255,411,6,7","text":"+"},{"boundingBox":"263,409,7,9","text":"U"}]},{"boundingBox":"233,432,38,10","words":[{"boundingBox":"233,432,38,10","text":"Ctrl+G"}]},{"boundingBox":"201,456,71,10","words":[{"boundingBox":"201,456,19,10","text":"Ctrl"},{"boundingBox":"223,459,6,7","text":"+"},{"boundingBox":"231,456,25,10","text":"Shift"},{"boundingBox":"258,459,6,7","text":"+"},{"boundingBox":"266,457,6,9","text":"L"}]}]}]}'
	match_arr = []
	for matching in re.finditer(pattern, json_str, re.I):
		match_arr.append(
			[int(matching.groups()[0]), int(matching.groups()[1]), int(matching.groups()[2]), int(matching.groups()[3]),
			 matching.groups()[4]])
	print(match_arr)


	def numeric_compare(x, y):
		return x - y

	match_arr = sorted(match_arr, key=lambda a:a[0]+a[1]/25*100000)
	print(match_arr)

except Exception as e:
	print("[Errno {0}] {1}".format(e.errno, e.strerror))
