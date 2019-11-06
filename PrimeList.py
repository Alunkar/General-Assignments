from MarvellousNum import ChkPrime;
def ListPrime():
	L= list()
	num = int(input("Enter Nomber of elements in List: "))
	print ("Enter numbers in List:  ")
	for i in range(num):
		no = int(input('number: '))
		L.append((no))
	print ('Entered elements are L: ',L);
	ChkPrime();

def main():
	ListPrime();

if __name__=="__main__":
	main();