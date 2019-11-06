def Summ():
	sum=v=z=0;
	v=int(input("Enter number: "));
	if v!=0 and v>0:
		while v>0:
			z=v%10;
			sum=int(sum+z);
			v=v/10;
		print(sum);
	else:
		print("Positve and Non zero only");
def main():
	Summ();

if __name__ == "__main__":
	main();