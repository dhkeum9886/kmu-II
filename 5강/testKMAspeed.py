# KMA analyzer speed test by Kang, Seung-Shik at Kookmin University
#
#		C> python testKMAspeed.py ITnews1000.txt
#		C> python testKMAspeed.py gtlee.txt

import sys

def load_file(filename):
#	f = open(filename, 'r', encoding='cp949')
	f = open(filename, 'r', encoding='utf-8')
	l = f.readlines()
	f.close()
	
	return l


from konlp.kma.klt2023 import klt2023
def test_KLT(text):
		klt = klt2023()

		outfile = 'output-KLT.txt'
		f = open(outfile, 'w')

		for aLine in text:
				kmaresult = klt.nouns(aLine.strip())
				for r in kmaresult:
						f.write(r+'\n')
		f.close()

		return outfile


from konlpy.tag import Okt
def test_Okt(text):
		okt = Okt()

		outfile = 'output-OKT.txt'
		f = open(outfile, 'w')

		for aLine in text:
				kmaresult = okt.nouns(aLine.strip())
				#print(kmaresult)
				for r in kmaresult:
						f.write(r+'\n')
		f.close()

		return outfile

from konlpy.tag import Kkma
def test_Kkma(text):
		kkma = Kkma()

		outfile = 'output-Kkma.txt'
		f = open(outfile, 'w')

		for aLine in text:
				kmaresult = kkma.nouns(aLine.strip())
				#print(kmaresult)
				for r in kmaresult:
						f.write(r+'\n')
		f.close()

		return outfile


import time

if __name__== '__main__':
		textFile = 'test.txt'

		if len(sys.argv)==2:
				textFile = sys.argv[1]
				outputFile = textFile.replace('.txt', '-KMA.txt')

		text = load_file(textFile)
		#print(text)

		startTime = time.time()
		outKLT = test_KLT(text)
		endingTime = time.time()
		print('Exec. time for KLT =', endingTime - startTime)

		startTime = time.time()
		outOKT = test_Okt(text)
		endingTime = time.time()
		print('Exec. time for OKT =', endingTime - startTime)

		startTime = time.time()
		outKkma = test_Kkma(text)
		endingTime = time.time()
		print('Exec. time for Kkma =', endingTime - startTime)

		print("KMA results are saved in", outKLT, outOKT, outKkma)

