import time

def sumofprimes(n):

	primeList=[True]*(n+1)

	p=2
	while(p*p<=n):
		if primeList[p]==True:
			i=p*2
			while i<n:
				 primeList[i]=False
				 i+=p
		p=p+1
	
	sum=0
	for i in range (2,n+1):
		if (primeList[i]):
			sum=sum+i

	return sum


if __name__ == '__main__':
	start=time.perf_counter()
	n=2000000
	sumVal=sumofprimes(n)
	print("Sum of Prime Numbers in range of {} is: {}".format(n,sumVal))
	print(f"Time Elapsed: {time.perf_counter()-start}") 
	