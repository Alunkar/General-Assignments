def star():
	x=int(input("Enter number: "))
	for i in range(x):
		print("* "*(x-i))

def main():
	star();

if __name__ == "__main__":
	main();