with open('euler011.txt','r') as files:
	array=[]
	for each in files:
		array.append(each)
		#print (each)
#print(array)

newArray=[]
for i in array:
	j=i.split(' ')
	k=[int(n) for n in j]
	newArray.append(k)
#print(newArray)
#print(newArray[0])

#print((newArray[0][0])*(newArray[1][1]))

maxprod=0
for i in range(16):
	for j in range(16):	
		prod_row=(newArray[i][j])*(newArray[i+1][j])*(newArray[i+2][j])*(newArray[i+3][j])
		if prod_row>maxprod:
			maxprod=prod_row
		prod_col=newArray[i][j]*newArray[i][j+1]*newArray[i][j+2]*newArray[i][j+3]
		if prod_col>maxprod:
			maxprod=prod_col
		prod_diag=newArray[i][j]*newArray[i+2][j+2]*newArray[i+2][j+2]*newArray[i+3][j+3]
		if prod_diag>maxprod:
			maxprod=prod_diag
		prod = newArray[19-i][j]*newArray[18-i][j+1]*newArray[17-i][j+2]*newArray[16-i][j+3]
		if prod>maxprod:
			maxprod=prod

print (maxprod)