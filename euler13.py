import time
def openfile():
	list_file=[]
	filepath = 'euler13.txt'  
	fline=open(filepath).readlines()
	summ_=0
	for each_line in fline:
		each_line=int(each_line)
		summ_+=each_line
	print('Sum of all the digits: {}'.format(int(summ_)))
	#print(fline)
	#extractList(fline)

if __name__ == '__main__':
	start=time.perf_counter()
	openfile()
	print(f'Total time taken : {time.perf_counter()-start}')

#Sum of all the digits: 5537376230390876637302048746832985971773659831892672
#Total time taken : 0.0040107819999999975