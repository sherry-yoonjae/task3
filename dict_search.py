# coding:utf-8
import time
dict1 = {}
def addWord(theIndex,word,pagenumber): 
  theIndex.setdefault(word, [ ]).append(pagenumber)
def search(dict1,element):
	if not dict1.has_key(element):
		return -1
	else:
		i = 0
		for ele in dict1:
			i = i + 1
			if(ele == element):
				return i
				
if __name__ == '__main__':
	start = time.time()
	for i in range(0,1000000):
		addWord(dict1,i,i)
	print search(dict1,999999)
	end = time.time()
	print("%f" %(end-start))