"""
Open input file and store in list 'masses'
"""
masses = []
raw = open("input_1.txt","r")
for line in raw:
    masses.append(int(line))
raw.close()

"""
Next step calculate the Fuel Total required as the puzzle answer for part one 'FT1'
To calculate fuel for each mass in masses:
Divide mass by 3
Take int of the result
Subtract 2
Add result to FT
"""

FT1 = 0
for mass in masses:
    fuel = int(mass/3)
    FT1 += (fuel - 2)

print("The answer to part 1 is " + str(FT1))

"""
Now the Fuelt Total 'FT2' must take into account the addition mass created by adding fuel
For each mass in masses, need to repeat the loop until the new fuel needed is <=0
Initially set fuel = mass as a dummy start
Then so long as fuel > 0, the loop continues
A check is made before adding fuel to the total in case it is negative on the last pass
"""

FT2 = 0
for mass in masses:
    fuel = mass
    while fuel > 0:
        fuel = (int(fuel/3)) - 2
        if fuel > 0:
            FT2 += fuel

print("The answer to part 2 is " + str(FT2))
