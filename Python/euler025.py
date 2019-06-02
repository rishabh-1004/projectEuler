import time

def fibonacci_number():
	a,b,c,counter=0,1,0,0
	while (len(str(c))!=1000):
		c=a+b
		a=b
		b=c
		counter+=1
	return counter+1

start=time.perf_counter()
s=fibonacci_number()
print(s)
print(f'Time Taken : {time.perf_counter()-start}')

#4782
#Time Taken : 0.059615099999064114