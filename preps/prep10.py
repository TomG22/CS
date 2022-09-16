string = input("Enter string:\n")

left_parenthesis = 0
right_parenthesis = 0
i = 0
while i < len(string):
  if string[i] == "(":
    left_parenthesis += 1
  elif string[i] == ")":
    right_parenthesis += 1
  if right_parenthesis > left_parenthesis:
    print("Parentheses unbalanced")
    exit()
  i += 1

if left_parenthesis == right_parenthesis:
  print("Parentheses balanced")
else:
  print("Parentheses unbalanced")
