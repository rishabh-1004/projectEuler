import time

start=time.perf_counter()

filename=open("p022_names.txt","r")
names=sorted(filename.read().replace('"','').split(','),key=str)
#print (names)
letters_dict={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,
				'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26 }

#names=["COLIN"]
total=0
sum_=0
for i in range (len(names)):
	for char in names[i]:
		value=letters_dict[char]
		sum_+=value
	total+=(sum_*(i+1))
#	if(i==937):
#		print(names[i], " " , (sum_*(i+1)))
	sum_=0
print (total)
print (f"Time taken {time.perf_counter()-start}")

#871198282
#Time taken 0.01878280000000001