import threading
import handwritten
hw=handwritten

class secure_class(object):
	def __init__(self):
		print('i',end='')
		self.lock=threading.Lock()

	def __getattribute__(self, name):
		print('g',end='')
		object.__getattribute__(self, 'lock').acquire()
		t=object.__getattribute__(self,name)
		object.__getattribute__(self, 'lock').release()
		return t
	'''
	def __getattr__(self, name):
		#这里只会进来__dict__里没有的成员
		self.lock.acquire()
		t=self._dic[name]
		self.lock.release()
		return t
	'''
	def __setattr__(self, name, value):
		print('s',end='')
		try:
			self.lock.acquire()
		except AttributeError:
			object.__setattr__(self,name,value)
		else:
			object.__setattr__(self,name,value)
			self.lock.release()

if __name__=='__main__':
	import json
	'''
	fo = open("conf.ini", "r")
	cof=json.load(fo)
	fo.close()

	img = open("E:/Users/Desktop/Atom/Edit.png", "rb")
	img_data=img.read()
	#li,_=hw.recognizeText(cof['base_url'],cof['subscription_key'],img_data	)
	img.close()
	for iten in li:
		print(iten)
	'''
	print('start')
	sc=secure_class()
	print(dir(sc))
	sc.ab=3

	print('QQ',sc.ab)