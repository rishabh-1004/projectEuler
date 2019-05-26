import os

def set_zeros(s):
	if (len(s)==3):
		return s
	elif(len(s)==2):
		return "0"+s
	else:
		return "00"+s

def main():
	file_names=os.listdir()
	for item in file_names:
		if(item[:5]=="euler")
		new_name=item[:5]+set_zeros(item[5:-3])+item[-3:]
		os.rename(item,new_name)

if __name__=="__main__":
	main()