import sys
"""
Open input file and store the two strings in "wires"
Create a list of instructions for each wire ("wireA","wireB") by splitting the
string in wires into individual instructions
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

"""
First, create a list of all co-ordinates WireA will pass through (circuitA)
This list starts at pos = (0,0) but does not include it as the puzzle does not care if the wires cross as (0,0).
Each instruction in WireA dictates how pos changes
U = add the value of WiresA[] to pos[1]
D = subtract from pos[1]
R = add to pos[0]
L = subtract from pos [0]
A check is made to ensure that if a wire passes through [0,0] it is ignored
Repeat for WireB in circuitB
Check circuitA against circuitB: if they contain the same co-ords at any point, store in list "cross"
When adding an item to cross, also store its Manhattan distance to the centre by taking sum of the absolute values of the co-ordinates
Sort cross by Manhattan values and return the lowest to answer part 1 of puzzle
"""
circuitA = []
circuitB = []
cross = []
def place_wire(wire,circuit):
    pos = [0,0]
    for w in wire:
        x = pos[0]
        y = pos[1]
        if w[0] == "U":
            while y < (pos[1] + w[1]):
                y +=1
                if pos[0] == 0 and pos[1] == 0:
                    continue
                else:
                    circuit.append([x,y])
            pos[1] += w[1]
        elif w[0] == "D":
            while y > (pos[1] - w[1]):
                y -=1
                if pos[0] == 0 and pos[1] == 0:
                    continue
                else:
                    circuit.append([x,y])
            pos[1] -= w[1]
        elif w[0] == "R":
            while x < (pos[0] + w[1]):
                x +=1
                if pos[0] == 0 and pos[1] == 0:
                    continue
                else:
                    circuit.append([x,y])
            pos[0] += w[1]
        elif w[0] == "L":
            while x > (pos[0] - w[1]):
                x -=1
                if pos[0] == 0 and pos[1] == 0:
                    continue
                else:
                    circuit.append([x,y])
            pos[0] -= w[1]
        else:
            sys.exit("Direction in wire A not recognised: " + str(wire[0]))
place_wire(wireA,circuitA)
place_wire(wireB,circuitB)
for coord in circuitA:
    if coord in circuitB:
        man = abs(coord[0])+abs(coord[1])
        cross.append([coord[0],coord[1],man])
cross.sort(key = lambda x: x[2])
print("The answer to part 1 is " + str(cross[0][2]))
