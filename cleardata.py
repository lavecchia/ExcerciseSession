import glob
import os



def findFiles(path):
	fileList = []
	for filename in glob.glob( os.path.join(path, '*.txt') ):
		fileList.append(filename)		
	return fileList
		
directory = "/afs/ictp.it/home/m/mlavecch/EJERCICIOS/COPY2TXT/cleandata"

print findFiles(directory)	