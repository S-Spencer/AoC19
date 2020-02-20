"""
Open input file and store the two strings in "wires"
Create a list of instructions for each wire ("wireA","wireB") by splitting the string in wires into individual instructions
Remove hanging "\n" from final instruction in WireA, WireB
Further split each instruction into a direction (U,D,L,R) and a distance
"""
wires = []
raw = open("input3.txt","r")
for line in raw:
    wires.append(line)
raw.close()
wireA = wires[0].split(",")
wireB = wires[1].split(",")
wireA[-1] = wireA[-1][:-1]
wireB[-1] = wireB[-1][:-1]
for i, wire in enumerate(wireA):
    wireA[i] = [wire[:1],int(wire[1:])]
for i, wire in enumerate(wireB):
    wireB[i] = [wire[:1],int(wire[1:])]
