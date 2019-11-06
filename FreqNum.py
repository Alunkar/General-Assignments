def Freq():
	num = int(input("Enter Nomber of elements in List: "))
	Ulist=list();
	print ("Enter numbers in List:  ")
	for i in range(num):
		no = int(input('number: '))
		Ulist.append((no))
	#print ('Entered elements are',Ulist)
	count=0;
	New = int(input('Search number: '))
	for value in Ulist:
		if New==value:
			count=count+1;
	print("Your Element is present: {} times".format(count));


def main():
	print("main")
	Freq();
	
if __name__=="__main__":
	main();