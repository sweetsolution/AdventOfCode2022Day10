##############################
# Advent of Code 2022
# Day 10, part b of puzzle
# Matthias, 2022-12-10
##############################

with open("input.txt") as f:
    contents = f.readlines()

register = 1
crt_pos = 0

def printchar(register, crt_pos):
    sprit_pos = {register-1,register,register+1}
    if (crt_pos in sprit_pos):
        print('#',end ='')
    else:
        print(".", end='')

def crt(register, crt_pos):
    printchar(register, crt_pos)
    crt_pos+=1
    if (crt_pos >=40):
        crt_pos = 0
        print()
    return crt_pos

for line in contents:
    command = line.split()
    if (command[0]=="noop"):
        crt_pos = crt(register, crt_pos)
    else:
        number = int(command[1])
        crt_pos = crt(register, crt_pos)
        crt_pos = crt(register, crt_pos)
        register +=number