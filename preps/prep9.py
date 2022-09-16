number = int(input("Enter factorial to calculate:\n"))

i = 0
factorial = 1
while i<number:
  i += 1
  factorial = factorial*i

print("\n"+str(number)+" factorial = "+str(factorial))