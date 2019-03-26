def Quick_sort(arr,st,fi):
	if fi <= st :
		return
	c = Find_c(arr,st,fi)
	print(arr,st,c)
	Quick_sort(arr,st,c-1)
	Quick_sort(arr,c+1,fi)
	
def Find_c(arr,st,fi):
	j = st						        #设置游标
	for i in range(st,fi+1):
		if arr[i] <= arr[fi]:
			temp = arr[j]
			arr[j] = arr[i]
			arr[i] =temp
			j += 1
		i += 1
		
	return j-1
	
arr = [4,5,7,2,6,8,1,3]
Quick_sort(arr,0,len(arr)-1)
print(arr)
