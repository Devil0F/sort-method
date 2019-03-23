'''冒泡排序法'''
def Bubble_sort(arr):
	n = len(arr)
	times = 0
	for i in range(0,n-1):
		sign = False
		for j in range(0,n-1-i):
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp 
				sign = True
			times = times+1
		print(arr,times)	
		if sign == False:
			break
		

arr = [8,5,3,5,7,1,2,10,8]
Bubble_sort(arr)
print(arr)	
