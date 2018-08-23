def binarySearch(arr,num,start,end):
	mid = (start + end) // 2
	if start <= end:
		if arr[mid] > num:
			return binarySearch(arr,num,start,mid-1)
		elif arr[mid] < num:
			return binarySearch(arr,num,mid+1,end)
		elif arr[mid] == num:
			return mid
	else:
		return -1
		

if __name__ == '__main__':
	arr = [1,3,4,6,8,19,28,33]
	result = binarySearch(arr,28,0,len(arr)-1)
	if result == -1:
		print("Element does not exist")
	else:
		print("Element present at position : " +str(result))