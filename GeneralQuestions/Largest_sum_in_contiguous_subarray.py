def maxSumContiguousSubarry(arr):
	start_index = -1
	end_index = -1
	max_sum_so_far = 0
	current_sum = 0
	set_start_index = -1
	i = 0
	while i < len(arr):
		if current_sum + arr[i] < 0:
			i = i + 1
		elif current_sum + arr[i] >= 0:
			if start_index == i == 0 and set_start_index == -1:
				start_index = i
				set_start_index = 1
			if start_index  < i and set_start_index == -1:
				start_index = i
				set_start_index = 1
			current_sum = current_sum + arr[i]
			if current_sum > max_sum_so_far:
				max_sum_so_far = current_sum
				end_index = i
			i = i + 1
			
	print("max sum is : " + str(max_sum_so_far))
	print("sub array is : "+str(arr[start_index:end_index+1]))
	#return 

if __name__ == '__main__':
	arr = [-1,2,4,-6,2,8,-10]
	maxSumContiguousSubarry(arr)
	