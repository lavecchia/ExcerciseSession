import inputdata
import numpy
from math import sqrt

	
# 1. Create a NumPy array with the recommendations	
class Personpaper(object):
	def __init__(self,data):
		pass
	
	#A python list where element i is the name of person i.
	def listPerson(self,data):
		persons = data.keys()
		return sorted(set(persons))
	
	#A python list where element j is the name of paper j.
	def listPaper(self,data):
		papers = []	
		for person, paper in data.items():
			for autor, calificacion in paper.items():
					papers.append(autor)
		return sorted(set(papers))
	
	#A numpy array where element i,j is the rating of person i for paper j.
	def arrayMaker(self):
		persons = self.listPerson(data)
		papers = self.listPaper(data)
		ij = numpy.zeros([len(persons),len(papers)], dtype=float)
		for i in range(0,len(persons)):
			for j in range(0,len(papers)):
				papersbyperson = data.get(persons[i], 0)
			 	valorbyautor = papersbyperson.get(papers[j], 0)
			 	ij[i,j] = valorbyautor
		return ij

	#Calculate Similarity

	#Calculate norm from two person	
	def normCalculate(self,user1,user2):
		index1 = self.listPerson(data).index(user1)
		index2 = self.listPerson(data).index(user2)
		elements = []	
		ij = self.arrayMaker()	
		for i in range(0,len(self.listPaper(data))): # I should have used logical_and for this instead
			#print str(i)+':'+str(ij[index1,i]) + "-"+ str(ij[index2,i]) 
			if ij[index1,i]>0 and ij[index2,i]>0:
				elements.append(ij[index1,i]-ij[index2,i])
		if len(elements)==0:
			return 0
		return numpy.linalg.norm(elements)
		
	#Calculate Pearson from two person	
	def pearsonCalculate(self,user1,user2):
		index1 = self.listPerson(data).index(user1)
		index2 = self.listPerson(data).index(user2)
		elements1 = []	
		elements2 = []
		ij = self.arrayMaker()	
		for i in range(0,len(self.listPaper(data))): # I should have used logical_and for this instead
			if ij[index1,i]>0 and ij[index2,i]>0:
				elements1.append(ij[index1,i])
				elements2.append(ij[index2,i])
		varcovar = numpy.cov(elements1, elements2)
		numerator = varcovar[0, 1]
		denominator = sqrt(varcovar[0, 0]) * sqrt(varcovar[1,1])
		if denominator == 0 or len(elements1)==0:
			return None
		r = numerator / denominator
  		return r
	
	
	#Generate a Recommendation
	
	#First, we could ask which researcher is most like you. Write a function that takes a researcher id and identifies the 5 researchers whose ratings are most like the researcher.
	def similartop5(self, user):
		similarusers = []
		for i in self.listPerson(data):
			if i != user:
				valor = self.normCalculate(user,i)
				similarusers.append([valor, i])
		similarusers.sort()
		if len(similarusers) > 5:
			return similarusers[:5] 
		else:
			return similarusers
	
	#the same of simiartop5 but return all users in order respect the similarity	
	def similarusers(self, user):
		similarusers = []
		for i in self.listPerson(data):
			if i != user:
				valor = self.normCalculate(user,i)
				similarusers.append([valor, i])
		similarusers.sort()
		return similarusers

	
	#Second, we could ask which papers have the most similar ratings. Write a function that takes a paper id and identifies the 5 paper whose ratings are most like the paper. 
	#Calculate norm from two papers	
	def normpaperCalculate(self,paper1,paper2): #I should reutiliced code and not cut and paste code, this must change!
		index1 = self.listPaper(data).index(paper1)
		index2 = self.listPaper(data).index(paper2)
		elements = []	
		ij = self.arrayMaker()	
		ij = ij.transpose()
		for i in range(0,len(self.listPerson(data))): # I should have used logical_and for this instead
			#print str(i)+':'+str(ij[index1,i]) + "-"+ str(ij[index2,i]) 
			if ij[index1,i]>0 and ij[index2,i]>0:
				elements.append(ij[index1,i]-ij[index2,i])
		if len(elements)==0:
			return None
		return numpy.linalg.norm(elements)
		
	def similarpapers(self,paper):
		similarpapers = []
		for i in self.listPaper(data):
			if i != paper:
				valor = self.normpaperCalculate(paper,i)
				similarpapers.append([valor, i])
		similarpapers.sort()
		if len(similarpapers) > 5:
			return similpapers[:5] 
		else:
			return similarpapers
				
	#Third, we could ask for recommended papers for a researcher. Write a function that identifies the top 5 papers that a researcher should read.
	def recommendation(self,user):
		recompapers = []
		listausers = self.similarusers(user) #search papers in the users more similar
		index1 = self.listPerson(data).index(user)
		ij = self.arrayMaker()		
		for i in listausers:
			print i			
			if i[1] != user:
				print "paso"
				index2 = self.listPerson(data).index(i[1]) # I should have used logical_and for this instead
				print len(self.listPaper(data))
				for j in range(0,len(self.listPaper(data))):
					if ij[index1,j]==0. and ij[index2,j]>0:
						if self.listPaper(data)[j] not in recompapers:
							recompapers.extend([self.listPaper(data)[j]])
						
		if len(recompapers) > 5:
			return recompapers[:5]
		else:
			return recompapers
				


data = inputdata.raw_scores
prueba = Personpaper(data)

print "norm:" + str(prueba.normCalculate('Mehrdad Mapping','Mehrdad Mapping'))  
print "Perason:" + str(prueba.pearsonCalculate('Mehrdad Mapping','Miguel Monopole'))  
print "similar users:" + str(prueba.similartop5('Miguel Monopole'))
print "similar papers:" + str(prueba.similarpapers('Jackson 1999'))
print "recommendation of papers:" + str(prueba.recommendation('Stephen Scanner'))