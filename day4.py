import sys
"""
This puzzle requires no input file. My two input values are 264360 and 746325
Need to sum the number of values between the inputs which also:
*contain at least one instance of two consecutive numbers being identical
*each consecutive digit must not be less than the previosu one
To facilitate easier comparison, the number shall be kept in a list "password"
passwords is initialised with the lower bound of values considered
"ul" is the upper limit, 746325
"lc" is the limit check, initially set to 264360. lc is checked again ul to keep loop going
Each time a password meets this criterial, "checked" is incrimented by +1
"""
password = [2,6,4,3,6,0]
ul = 746325
lc = 264360
checked = 0
"""
"increase" is a function to increase the password value by +1
It requires a list and the index of the value to be increased (which will normally be 5)
If the value of an index is 9 (which would mean increasing to 10), increase calls itself but one index to the left
To avoid error, in any instance where index = 0 is trying to increase above 9, the program is halted
"""
def increase(list,index):
    if list[index] == 9:
        if index == 0:
            sys.exit("Password value overflow! Closing program")
        else:
            list[index] = 0
            increase(list,index-1)
    else:
        list[index] += 1

"""
Passwords are checked against criteria.
fail1 counts the number of times a number fails the first criteria (each digit must be <= the following digit)
pass2 counts how many times a number passes the second criteria (a password must contain atleast one instance of two identical digits next to each other)
i and j are counting variables
First the digits in tha password are checked against first criteria. If they fail fail1 is incremented
THe second check is only preformed on passwords that did not fail the first criteria ie fail1 == 0
THen the number of instances for each password passing the second criteria are stored in pass2
So long as a password has pass2 > 1, checked is increased
At the end of each check, both lc and the list password are increased by 1
"""
while lc < ul:
    fail1 = 0
    pass2 = 0
    i = 0
    j = 0
    while i < 5:
        if password[i] > password[i+1]:
            fail1 += 1
        i +=1
    if fail1 == 0:
        while j < 5:
            if password[j] == password[j+1]:
                pass2 += 1
            j += 1
    if pass2 > 0:
        checked += 1
    increase(password,5)
    lc += 1
print("The answer to part 1 is " + str(checked))
