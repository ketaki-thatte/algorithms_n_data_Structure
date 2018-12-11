def mergeSort(arr):

	n = len(arr)
	if n  < 2:
		return arr
	mid = n//2
	left_arr = []
	right_arr = []
	for left_ptr in range(0,mid):
		left_arr.append(arr[left_ptr])
	for right_ptr in range(mid,n):
		right_arr.append(arr[right_ptr])
	mergeSort(left_arr)
	mergeSort(right_arr)
	merge(left_arr,right_arr,arr)


def merge(left,right,arr):
	nl = len(left)
	nr = len(right)
	n = len(arr)
	k = 0
	i = 0
	j = 0
	while i < nl and j <nr:
		if left[i] <= right[j]:
			arr[k] = left[i]
			i = i + 1
		else:
			arr[k] = right[j]
			j = j + 1
		k = k+1
	while i <nl:
		arr[k] = left[i]
		i = i + 1
		k = k+1
	while j < nr:
		arr[k] = right[j]
		j = j + 1
		k = k+1

if __name__ == '__main__':
	arr = [1,24,0,8,91,33,12,87]
	mergeSort(arr)
	print(arr)