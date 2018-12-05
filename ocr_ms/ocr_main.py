import threading
import handwritten as hw
import sys

class secureIter_C(object):
	def __init__(self,li=[]):
		self.lock=threading.Lock()
		self._it=iter(li)
	def next(self):
		self.lock.acquire()
		t=next(self._it)
		self.lock.release()
		return t

def put_arr(a):
	for i in a:
#		print(type(i))
		print('\''+str(i)+'\'')
	print('')

class ocrThread_C(threading.Thread):
	def __init__(self,base_url,subscription_key,file_name_iter):
		threading.Thread.__init__(self)
		self._base_url=base_url
		self._subscription_key=subscription_key
		self._file_name_iter=file_name_iter

	def run(self):
		while True:
			try:
				file_name=self._file_name_iter.next()
			except:
				return
			img = open(file_name, "rb")
			img_data = img.read()
			img.close()
			retry = 0
			while True:
				try:
					li, _ = hw.recognizeText(self._base_url, self._subscription_key, img_data)
					break
				except hw.requests.exceptions.ConnectionError:
					#网络没有连接
					put_arr(sys.exc_info())
					retry+=1
					if retry>20:
						return



if __name__=='__main__':
	import json

	''''''
	fo = open("conf.ini", "r")
	cof=json.load(fo)
	fo.close()


