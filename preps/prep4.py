feet = int(input("Number of feet:\n"))
inches = feet*12
meters = round(feet*.3048,3)
rods = round(feet/16.5,1)

print(f'\nInches: {inches}\nMeter: {meters}\nRods: {rods}')
