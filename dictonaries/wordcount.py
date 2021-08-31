S = str(input())  
str = S.split()
tempS=[]
for i in str:              
	if i not in tempS: 
		tempS.append(i)
 
for i in range(0, len(tempS)):
	print("%1s:%2s"%(tempS[i].ljust(1),str.count(tempS[i])))  