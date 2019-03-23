def Insertion_Sort(arr):
	n = len(arr)
	times = 0
	for i in range(1,n):
		value = arr[i]
		for j in range(i-1,-1,-1):
			if arr[j] > value:
				arr[j+1] = arr[j]
				arr[j] = value
				times = times+1
			else:

				break
		print(arr,times)
arr = [8,5,3,5,7,1,2,10,8]
Insertion_Sort(arr)
print(arr)
