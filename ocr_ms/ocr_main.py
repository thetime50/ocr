import threading
import handwritten as hw
import sys

class secureDict_C(object):
	def __init__(self,*args):
		self.lock=threading.Lock()
		self._dic={}
		self.set(*args)
	def get(self,*args):
		self.lock.acquire()
		if len(args)==0:
			t=self._dic
		elif len(args)==1:
			t=self._dic[args[0]]
		self.lock.release()
		#这里还需要考虑一下参数的生命空间
		return t
	def set(self,*args):
		self.lock.acquire()
		if len(args)==1 and type(args[0])==type({}):
			for key in args[0]:
				self._dic[key]=args[0][key]
		elif len(args)==2:
			self._dic[args[0]] = args[1]
		self.lock.release()

	#sd=secureDict_C({0:3})
	#sd.set(2,2)
	#sd.set({6:7,8:9})
	#print(sd.get(0),sd.get(2),sd.get())#

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
	from io import BytesIO

	img = open("E:/Users/Desktop/Atom/Edit.png", "rb")
	img_data=img.read()
	img.close()

	try:
		li,_=hw.recognizeText(cof['base_url'],cof['subscription_key'],img_data	)
		for iten in li:
			print(iten)
	except:
		put_arr(sys.exc_info())

