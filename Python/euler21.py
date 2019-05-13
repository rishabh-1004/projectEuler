import time

def sum_of_divisors(n):
	sum_=0
	for i in range(1,n//2+1):
		if(n%i==0):
			sum_+=i
	
	return sum_

def main():
	list1=[]
	sum_=0
	for i in range(1,10_000):
		s=sum_of_divisors(i)
		r=sum_of_divisors(s)
		#print(s,r,i)
		if(r==i and i!=s):
			sum_+=i

	print(sum_)
if __name__=='__main__':
	start=time.perf_counter()
	main()
	print(f'Time taken: {time.perf_counter()-start} s')

#31626
#Time taken: 4.788672888000001 s