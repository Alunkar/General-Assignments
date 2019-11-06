def ChkInt():
	num= int(input("Enter any numer: "));
	if num>0:
		print("Positive Number :", num);
	elif num==0:
		print("Its a Zero");
	else:
		print("Negative Number :", num);

def main():
	ChkInt();

if __name__ == "__main__":
	main();