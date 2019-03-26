def Selection_sort(arr):
	n = len(arr)
	times = 0
	for i in range(n):
		for j in range(i,n):
			times = times+1	
			if arr[j] == min(arr[i:]):
				temp = arr[i]
				arr[i] = arr[j]
				arr[j] = temp			
				break
		print(arr,times)		
arr = [8,5,3,5,7,1,2,10,8]
Selection_sort(arr)
print(arr)
