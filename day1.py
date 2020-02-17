"""
Open input file and store in list 'masses'
"""
masses = []
raw = open("input_1.txt","r")
for line in raw:
    masses.append(int(line))
raw.close()

"""
Next step calculate the Fuel Total required as the puzzle answer for part one 'FT'
To calculate fuel for each mass in masses:
Divide mass by 3
Take int of the result
Subtract 2
Add result to FT
"""

FT = 0
for mass in masses:
    fuel = int(mass/3)
    FT += (fuel - 2)

print("The answer to part 1 is" + str(FT))
