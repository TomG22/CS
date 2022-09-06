temp = int(input("Temperature in fahrenheit:\n"))

if temp <= 32:
  print("Ice")
elif 32 < temp < 212:
  print("Water")
else:
  print("Steam")