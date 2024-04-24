def primeornot(n):
	factorslist = []
	for i in range(1,n+1):
		if n%i == 0:
			factorslist.append(i)
	print(f"The Factors are: {factorslist}")
	if len(factorslist) == 2:
		print(f"The number {n} is prime")
	else:
		print(f"The number {n} is not prime")
n = int(input("Enter the number: "))
primeornot(n)
