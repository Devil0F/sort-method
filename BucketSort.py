def Bucket_sort(arr):
	n = len(arr)
	print(arr)
	a,b,c,d,e,f,g,h,k,j = [],[],[],[],[],[],[],[],[],[]
	for i in range(0,n):
		if arr[i] < 10:
			a.append(arr[i])
		elif arr[i] < 20:
			b.append(arr[i])
		elif arr[i] < 30:
			c.append(arr[i])
		elif arr[i] < 40:
			d.append(arr[i])
		elif arr[i] < 50:
			e.append(arr[i])
		elif arr[i] < 60:
			f.append(arr[i])
		elif arr[i] < 70:
			g.append(arr[i])
		elif arr[i] < 80:
			h.append(arr[i])
		elif arr[i] < 90:
			k.append(arr[i])
		elif arr[i] <= 100:
			j.append(arr[i])
	del arr[:]
	for i in [a,b,c,d,e,f,g,h,k,j]:
		Quick_sort(i,0,len(i)-1)
		arr.extend(i)
def Quick_sort(arr,st,fi):
	if fi <= st :
		return
	c = Find_c(arr,st,fi)
	Quick_sort(arr,st,c-1)
	Quick_sort(arr,c+1,fi)
	
def Find_c(arr,st,fi):
	j = st						
	for i in range(st,fi+1):
		if arr[i] <= arr[fi]:
			temp = arr[j]
			arr[j] = arr[i]
			arr[i] =temp
			j += 1
		i += 1
		
	return j-1
import random
arr = []
for i in range(100):
	arr.append(random.randint(1,100))
Bucket_sort(arr)
print(arr)
		
	
