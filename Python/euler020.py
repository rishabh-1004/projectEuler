import time

def factorial(n):
	total=1
	for i in range(1,n+1):
		total*=i
	return total

def main():
	number=100
	sum_=0
	fact=factorial(number)
	print(fact)
	sum_list=list(str(fact))
	for x in sum_list:
		sum_+=int(x)
	print(sum_)

if __name__=='__main__':
	start=time.perf_counter()
	main()
	print(f"Total time taken  : {time.perf_counter()-start}")

#93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
#648
#Total time taken  : 0.0005761719999999998