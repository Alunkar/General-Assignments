def Min():
	num = int(input("Enter Nomber of elements in List: "))
	Ulist=list();
	print ("Enter numbers in List:  ")
	for i in range(num):
		no = int(input('number: '))
		Ulist.append((no))
	print ('Entered elements are',Ulist)
	c=Ulist[0];
	for value in Ulist:
		if c >= value:
			c=value;
	print(c)

def main():
	print("main")
	Min();
	
if __name__=="__main__":
	main();