from functools import reduce;

def ChkPrime():
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
		Add=reduce(lambda no1,no2: no1+no2,NewL)
	print(Add);
