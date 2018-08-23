def decToBin(num):
	arr = []
	while num > 0:
		print([num%2])
		arr = [num%2] + arr
		num = num//2
	arr = [num] + arr
	return ''.join(str(i) for i in arr) 

	

if __name__ == '__main__':
	print(decToBin(4))