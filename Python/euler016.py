import time 
start=time.perf_counter()

num=2**1000
sum_=0
while(num>0):
	n=num%10
	sum_=sum_+n
	num=num//10
print(sum_)
print(f"Time taken :{ time.perf_counter() -start}")

#1366
#Time taken :0.0006218859999999951s