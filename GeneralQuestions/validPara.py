def generateParathesis(n):
	if n%2 == 0:
		print(validPara(n//2,n//2,""))
	else:
		return [""]
def validPara(openB,closeB,string):
	arr = []
	if openB == closeB == 0:
		arr.append(string)
	if (openB > closeB):
		arr.append(string)
	if (openB > 0):
		validPara(openB - 1, closeB, string + "("); 
		print(string)
	if (closeB > 0):
		validPara(openB, closeB - 1, string + ")");
		print(string)
	return arr

if __name__ == '__main__':
	generateParathesis(2)