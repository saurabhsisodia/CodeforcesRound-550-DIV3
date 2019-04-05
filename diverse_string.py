from collections import defaultdict
def fun(string):
	l=len(string)
	fre=[0]*26
	array=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	d=defaultdict(int)
	s="abcdefghijklmnopqrstuvwxyz"
	for i in range(26):
		d[s[i]]=i
	for v in string:
		x=d[v]
		fre[x]+=1
	if max(fre)>1:
		return "NO"
	for i in range(26):
		if fre[i]!=0:
			start=i
			break
	for i in range(start,26):
		if fre[i]==0 and l!=0:
			return "No"
		l-=1
		if l==0:
			return "YES"


		


t=int(input())
while t>0:
	string=input()
	print(fun(string))
	t-=1
