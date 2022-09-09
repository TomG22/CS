size = input("Drink Size:\n")
type = input("Drink type:\n")

calories = 0

if type == "regular" and size == "large":
  calories = 300
elif type == "regular" and size == "small":
  calories = 150
elif type == "diet" and size == "large":
  calories = 100
elif type == "diet" and size == "small":
  calories = 50

print("\n"+str(calories)+" calories")