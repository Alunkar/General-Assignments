def Fact():
	f=1;
	num=int(input("Enter Number: "));
	if num>0:
		for i in range(1,num+1):
			f=f*i;
		print(f);
	else:
		print("Enter Positive Non Zero number");

def main():
	Fact();

if __name__ == "__main__":
	main();