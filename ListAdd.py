from functools import reduce;

def main():

	L = list()
	num = int(input("Enter Nomber of elements in List: "))
	print ("Enter numbers in List:  ")
	for i in range(num):
		no = int(input('number: '))
		L.append((no))
	print ('Entered elements are',L)
	Sum=reduce(lambda no1,no2 : no1+no2, L)
	print(Sum);


if __name__ == "__main__":
	main();