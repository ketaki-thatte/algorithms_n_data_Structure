def generatePara(n):
	return validPara(n,0,"",[])
	
def validPara(openB,closeB,curr,arr):
	if openB==0 and closeB == 0:
		arr.append(curr)
	if openB > 0:
		validPara(openB-1,closeB+1,curr+"(",arr)
	if closeB > 0:
		validPara(openB,closeB-1,curr+")",arr)
	return arr

if __name__ == '__main__':
	print(generatePara(3))