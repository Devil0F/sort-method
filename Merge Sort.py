def Merge_sort(arr,st,n):            #arr也随着每次调用发生变化
	if n-1<=st:
		return arr
	arr_l = arr[:((n-1)/2)+1]    #切片末端不包含，故此处+1
	arr_r = arr[((n-1)/2)+1:]
	Merge_sort(arr_l,0,len(arr_l))
	Merge_sort(arr_r,0,len(arr_r))
	arr = Merge(arr,arr_l,arr_r)
	return arr
	
	
	
def Merge(arr,arr_l,arr_r):
	i,j,k= 0,0,0
	temp = arr
	while i != len(arr_l) and j != len(arr_r):
		if arr_l[i] > arr_r[j]:
			temp[k] = arr_r[j]
			k = k+1
			j = j+1
		else:
			temp[k] = arr_l[i]
			k = k+1
			i = i+1
	if i == len(arr_l):				#将剩余数据拷贝给temp
		temp[k:] = arr_r[j:]
	else:
		temp[k:] = arr_l[i:]
	arr = temp
	return arr
	
arr = [6,4,8,1,4,2,7,6]
arr=Merge_sort(arr,0,len(arr))
print(arr)
