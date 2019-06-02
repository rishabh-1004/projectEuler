import time
start = time.perf_counter()
sequence_Length=0
number=0
for i in range(1000,1,-1):
	if(sequence_Length>=i):
		break
	foundRemainders=[0]*i

	value=1
	position=0

	while(foundRemainders[value]==0 and value!=0):
		foundRemainders[value]=position
		value*=10
		value%=i
		position+=1

	if(position-foundRemainders[value]>sequence_Length):
		number=i
		sequence_Length=position-foundRemainders[value]

#print (sequence_Length)
print(number)
print(f'Time taken : {time.perf_counter()-start} ')

#983
#Time taken : 0.002524999999877764