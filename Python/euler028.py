

values=[]
values.append(1)
current=1
counter=2
for i in range(100001):
	for _ in range(4):
		values.append(current+counter)
		current=current+counter
	counter+=2
	if(current==100201):
		break
print(sum(values))