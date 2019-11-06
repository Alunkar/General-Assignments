def main():
	global L 
	L= list()
	num = int(input("Enter Nomber of elements in List: "))
	print ("Enter numbers in List:  ")
	for i in range(num):
		no = int(input('number: '))
		L.append((no))
	print ('Entered elements are L: ',L);
	Prm();

def Prm():
	NewL=[]
	for x in L:
		if x==2 or x==3:
			NewL.append(x)

		if x>3:
			for i in range(1,x):
				if	(6*i)-1==x:
					NewL.append(x)

				if	(6*i)+1==x:
					NewL.append(x)
	print("Prime numbers are: ",NewL)

if __name__=="__main__":
	main();