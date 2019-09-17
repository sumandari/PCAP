def isPrime(num):
    devider = [2,3,4,5,6,7,8,9]
    for n in devider:
        if num % n == 0 and num // n != 1:
            return False
    return True

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
