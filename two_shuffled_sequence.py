from collections import defaultdict
d=defaultdict(int)
def check_existence(array):
	for v in array:
		d[v]+=1
	if max(d.values())>2:
		return 0
	else:
		return 1
def fun(array,n):
	strictly_incr=[]
	strictly_decr=[]
	check=check_existence(array)
	if check==0:
		print("NO")
	else:
		array.sort()
		for i in range(n):
			if len(strictly_incr)==0 or strictly_incr[-1]!=array[i]:
				strictly_incr.append(array[i])
			else:
				strictly_decr.append(array[i])
	if check==1:
		print("YES")
		if len(strictly_incr)==0:
			print(0)
			print(" ")
		else:
			print(len(strictly_incr))
			print(*strictly_incr)
		if len(strictly_decr)==0:
			print(0)
			print(" ")
		else:
			print(len(strictly_decr))
			print(*strictly_decr[::-1])
n=int(input())
array=list(map(int,input().split( )))
fun(array,n)
