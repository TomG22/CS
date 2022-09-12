#
# Author: Tom Giallanza
# Course: CSC 110
# Description: This program breaks down annual finances based on salary and expenses. 
# Answer the prompts and the breakdown will be printed. Warnings are built in.
#

print('''-----------------------------
----- WHERE'S THE MONEY -----
-----------------------------''')

salary = input("What is your annual salary?\n")
if salary.isnumeric() == False:
  print("Must enter positive integer for salary.")
  exit()

rent = input("How much is your monthly mortgage or rent?\n")
if rent.isnumeric() == False:
  print("Must enter positive integer for mortgage or rent.")
  exit()

bills = input("What do you spend on bills monthly?\n")
if bills.isnumeric() == False:
  print("Must enter positive integer for bills.")
  exit()

food = input("What are your weekly grocery/food expenses?\n")
if food.isnumeric() == False:
  print("Must enter positive integer for food.")
  exit()

travel = input("How much do you spend on travel annually?\n")
if travel.isnumeric() == False:
  print("Must enter positive integer for travel.")
  exit()

salary = int(salary)
rent = int(rent)*12
bills = int(bills)*12
food = int(food)*52
travel = int(travel)
tax = None

if 0 < salary <= 15000:
  tax = 0.10
elif 15000 < salary <= 75000:
  tax = 0.20
elif 75000 < salary <= 200000:
  tax = 0.25
else:
  tax = 0.30

tax = salary*tax
if tax > 75000:
  tax = 75000

expenses = rent+bills+food+travel
extra = salary-(expenses+tax)
greatest = max(int((rent/salary)*100), 
               int((bills/salary)*100), 
               int((food/salary)*100), 
               int((travel/salary)*100), 
               int((tax/salary)*100), 
               int((extra/salary)*100))

print('\n'+''+'------------------------------------------'+'-'*(greatest)+
      '\nSee the financial breakdown below, based on a salary of $'+str(salary)+
      '\n'+''+'------------------------------------------'+'-'*(greatest)+
      '\n| mortgage/rent | $'+format(rent, '9,.2f')+ ' |  '+format((rent/salary)*100, '4,.1f')+'% | '+'#'*int((rent/salary)*100)+
      '\n|         bills | $'+format(bills, '9,.2f')+ ' |  '+format((bills/salary)*100, '4,.1f')+'% | '+'#'*int((bills/salary)*100)+
      '\n|          food | $'+format(food, '9,.2f')+ ' |  '+format((food/salary)*100, '4,.1f')+'% | '+'#'*int((food/salary)*100)+
      '\n|        travel | $'+format(travel, '9,.2f')+ ' |  '+format((travel/salary)*100, '4,.1f')+'% | '+'#'*int((travel/salary)*100)+
      '\n|           tax | $'+format(tax, '9,.2f')+ ' |  '+format((tax/salary)*100, '4,.1f')+'% | '+'#'*int((tax/salary)*100)+
      '\n|         extra | $'+format(extra, '9,.2f')+ ' |  '+format((extra/salary)*100, '4,.1f')+'% | '+'#'*int((extra/salary)*100)+
      '\n'+'------------------------------------------'+'-'*(greatest))

if tax >= 75000:
  print(">>> TAX LIMIT REACHED <<<")

if salary < expenses+tax:
  print(">>> WARNING: DEFICIT <<<")
