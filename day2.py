"""
Opens input file
Breaks string up into individual instructions and stores in list "instructions"
"""
raw = open("input_2.txt","r")
instructions = (raw.read()).split(",")
raw.close()
instructions = list(map(int, instructions))
inst = instructions.copy()
"""
As per part 1 of puzzle, set instructions [1] and [2] to 12 and 2 respectively
"""
instructions[1] = 12
instructions[2] = 2
"""
Solve the puzzle for part one:
THe entire list is checked over once, hence the need for the length of the list
4 consecutive entries in the list are read at once and used as input
The first determines the action to be taken, then next two the position in the list of the inputs, and the final where in the list to store the output
If the action is "1", the inputs are added
If the action is "2", the inputs are multiplied
If the action is "99" then the program terminates, giving the first value in the list as its final answer
Any other action is invalid and recoreded as an error
"""
length = len(instructions)
i = 0
while i < (length-2):
    if instructions[i] == 1:
        pos1 = instructions[i+1]
        pos2 = instructions[i+2]
        pos3 = instructions[i+3]
        temp = instructions[pos1]+instructions[pos2]
        instructions[pos3] = temp
    elif instructions[i] == 2:
        pos1 = instructions[i+1]
        pos2 = instructions[i+2]
        pos3 = instructions[i+3]
        temp = instructions[pos1]*instructions[pos2]
        instructions[pos3] = temp
    elif instructions[i] == 99:
        print("Opcode 99: Program complete!")
        print("The answer to part 1 is " + str(instructions[0]))
    else:
        print("Invalid opcode: " + str(instructions[i]) + ", program terminating")
        print(i)
        break
    i += 4

"""
Part 2
As part one, but now need to test different value for instructions[1] and [2] that give a result of 19690720
noun and verb are used as different values of instructions[1] and [2] respectively
Each pass requires instructions to be reset to their original value as originally input. Use a copy inst of the original unaltered input for this
"""
noun = 0
verb = 0
while noun < 100:
    while verb < 100:
        instructions = inst.copy()
        instructions[1] = noun
        instructions[2] = verb
        i = 0
        while i < (length-2):
            if instructions[i] == 1:
                pos1 = instructions[i+1]
                pos2 = instructions[i+2]
                pos3 = instructions[i+3]
                temp = instructions[pos1]+instructions[pos2]
                instructions[pos3] = temp
            elif instructions[i] == 2:
                pos1 = instructions[i+1]
                pos2 = instructions[i+2]
                pos3 = instructions[i+3]
                temp = instructions[pos1]*instructions[pos2]
                instructions[pos3] = temp
            elif instructions[i] == 99:
                if instructions[0] == 19690720:
                    ans = (100*noun)+verb
                    print(" The answer to part 2 is " + str(ans))
                    noun = 101
                    verb = 101
                else:
                    break
            else:
                break
            i += 4
        verb += 1
    noun += 1
    verb = 0
