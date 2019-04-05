def fun(array,n):
	odd,even=[],[]
	l_odd,l_even=0,0
	for v in array:
		if v%2==0:
			even.append(v)
			l_even+=1
		else:
			odd.append(v)
			l_odd+=1
	if l_odd==0:
		even.sort()
		return sum(even[:l_even-1])
	if l_even==0:
		odd.sort()
		return sum(odd[:l_odd-1])
	odd.sort()
	even.sort()
	if (l_odd==l_even) or (l_odd==l_even+1 or l_even==l_odd+1):
		return 0
	elif l_odd>l_even:
		return sum(odd[:l_odd-l_even-1])
	else:
		return sum(even[:l_even-l_odd-1])

n=int(input())
array=list(map(int,input().split( )))
print(fun(array,n))