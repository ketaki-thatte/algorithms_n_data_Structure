import time
def bruteForceMethod(string,pattern):
	start_time = time.time()
	n =len(pattern)
	i = 0	

	print(string)
	while  i <len(string):
		# print(string[i:(i+n)])
		if string[i:(i+n)] == pattern:
			print(i)
		i = i+1		
	end_time = time.time()
	return end_time-start_time
	#print("max sum is : " + str(max_sum_so_far))

	
def KMPAlgorithm(string,pattern):
	# longest pattern prefix which is also a suffix
	arr  = buildLPS(pattern)
	j = 0
	for i in range(0,len(string)):
		while (j > 0 and string[i] != pattern[j]):
			j = arr[j - 1];   #Strictly decreasing
			if string[i] == pattern[j]:
				j = j + 1
				if (j == len(pattern)):
					print("pattern found at : " + (i - (j - 1)))
	return -1;  #// Not found

def buildLPS(string):
	arr = [0] *(len(string))
	i = 0
	j = 1
	while j < len(string):
		if string[i] == string[j]:
			arr[j] = i + 1
			j = j+1
			i = i+1
		else:
			if i != 0:
				i = arr[i-1]
			
			else:
				arr[j] = 0
				j = j + 1
	return arr
def calculateHash(stringToCal):
	prime_number = 2
	hash_value = 0
	for i in range(0,len(stringToCal)):
		hash_value =  hash_value + (ord(stringToCal[i]) * 2**(i))
	return hash_value

def matchBothStrings(strg,pat):
	for i in range(0,len(strg)):
		if strg[i] != pat[i]:
			return False
	return True

def RabinKarpAlgo(string,pattern):
	start_time =time.time()
	pattern_hash = calculateHash(pattern)	
	p_len = len(pattern)
	s_len = len(string)
	i = 0
	string_hash = calculateHash(string[0:p_len])
	while i < s_len-p_len:
		if (i > 0):
			prev_char = i-1
			prev_val = (ord(string[i-1]))
			next_char_val = (ord(string[(prev_char+p_len)]) * (2**(p_len-1))) 
			
			string_hash = ((string_hash - prev_val)//2 ) + next_char_val 

		if string_hash == pattern_hash:
			if(matchBothStrings(string[i:(i+p_len)],pattern)):
				print("Found Matching string at : "+ str(i))
		i = i + 1
	end_time =time.time()
	return end_time-start_time
if __name__ == '__main__':
	# string = 'AACAACAABAACAAADAA'
	string = 'AABAABAC'
	pattern = 'AABA'
	print(bruteForceMethod(string,pattern))
	KMPAlgorithm('AABAABAAA',pattern)
	#O(m+n) but worst case O(mn) when all characters are same
	print(RabinKarpAlgo('AABAABAC','AABA'))