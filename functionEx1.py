import glob
import os

'''find all txt files in path and return a list with their names'''
def findFiles(path):
	fileList = []
	for filename in glob.glob( os.path.join(path, '*.txt') ):
		fileList.append(filename)		
	return fileList
		
'''return True or False if there is N or not is in sex item respectively in filename'''
def findfileN(filename): 
	status = False	
	file = open(filename, 'r')
	for line in file:
		if "Sex: N" in line:
			status = True
	file.close()
	return status

'''return True or False if there is N or not is in line'''
def findNinline(line): 
	status = False	
	if "Sex: N" in line:
			status = True
	return status	

'''replace in a line N to M'''
def replaceN2M(filename):
	status = False	#save if this file contain N
	file=open(filename,'r')
	filecontent=[]
	for line in file:
		if findNinline(line)==True:
			line = "Sex: M"
			status = True #yes, this file contain N
		filecontent.append(line)
	file.close()
	if status == True:
		file=open(filename, 'w')
		for line in filecontent:
			file.write(line+"\n")
		file.close()				
			 

'''test findFiles function'''
#directory = "/afs/ictp.it/home/m/mlavecch/EJERCICIOS/COPY2TXT/cleandata"
#print findFiles(directory)	

'''test findN function'''
#lista = findFiles(directory)
#for i in lista:
#	print i + " " + str(findfileN(i))

'''test replaceN2M function'''
#for i in lista:
#	replaceN2M(i)


