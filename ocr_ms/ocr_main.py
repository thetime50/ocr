import threading
import handwritten as hw
import sys
import os

class secureIter_C(object):
	def __init__(self,li=[]):
		self.lock=threading.Lock()
		self._it=iter(li)
	def next(self):
		self.lock.acquire()
		try:
			t=next(self._it)
		finally:
			self.lock.release()
		return t

def put_arr(a):
	for i in a:
#		print(type(i))
		print('\''+str(i)+'\'')
	print('')


securePrintLock = threading.Lock()
def securePrint(*a):
	securePrintLock.acquire()
	print(*a)
	securePrintLock.release()


class ocrThread_C(threading.Thread):
	def __init__(self,id,base_url,subscription_key,file_name_iter):
		threading.Thread.__init__(self)
		self._id=id
		self._base_url=base_url
		self._subscription_key=subscription_key
		self._file_name_iter=file_name_iter

	def run(self):
		threadStr='oT:'
		securePrint(threadStr,self._id)
		while True:
			try:
				file_name=self._file_name_iter.next()
				securePrint(threadStr, self._id,'ocr file:',file_name)
			except:
				securePrint(threadStr, self._id,'file_iter empty')
				return
			img = open(file_name, "rb")
			img_data = img.read()
			img.close()
			retry = 0
			while True:
				try:
					li, _ = hw.recognizeText(self._base_url, self._subscription_key, img_data)
					fout=open(file_name.split('.')[0]+'.txt','a+')
					for item in li:
						fout.write(item+'\r\n')
					fout.close()
					break
				except hw.requests.exceptions.ConnectionError:
					#网络没有连接
					put_arr(sys.exc_info())
					retry+=1
					if retry>20:
						print(threadStr, self._id, 'connect error')
						return
					elif retry % 3==0:
						print(threadStr, self._id, 'retry',retry)



if __name__=='__main__':
	import json
	print(sys.argv[0],'Start')
	''''''
	fo = open(sys.path[0]+"/conf.ini", "r")
	cof=json.load(fo)
	fo.close()

	ftype=('PEG','JPEG', 'PNG', 'GIF', 'BMP')
	file_list=[]
	for item in sys.argv[1:]:
		if os.path.isfile(item) and item.split('.')[-1].upper() in ftype:
			file_list.append(item)

	ocrThreadMax=25
	print('ocrThreadMax:',ocrThreadMax)
	print('files:',len(file_list))
	for item in file_list:
		print(item)
	print('\r\n')
	print('***************************************************')

	if ocrThreadMax>len(file_list):
		ocrThreadMax=len(file_list)

	sfile_iter=secureIter_C(file_list)
	thread_list=[]
	for item in range(ocrThreadMax):
		thread_list.append(\
			ocrThread_C(item,cof['base_url'],cof['subscription_key'],sfile_iter))
	for item in thread_list:
		item.start()
	for item in thread_list:
		item.join()
	print(sys.argv[0],'End')


