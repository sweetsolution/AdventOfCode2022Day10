##############################
# Advent of Code 2022
# Day 10, part a of puzzle
# Matthias, 2022-12-10
##############################

with open("input.txt") as f:
    contents = f.readlines()

cycle_read_target = 20
multiplier = [20, 60, 100, 140, 180, 220]
mulcnt = 0
cyclecounter = 0
register = 1
signalsum = 0


def signal_strength(cyclecounter, cycle_read_target, mulcnt, signalsum):
    cyclecounter += 1
    if cyclecounter == cycle_read_target:
        signalsum +=register * multiplier[mulcnt]
        cycle_read_target+=40
        mulcnt+=1
    return cyclecounter, signalsum, cycle_read_target, mulcnt

for line in contents:
    command = line.split()

    if (command[0]=="noop"):
        cyclecounter, signalsum, cycle_read_target, mulcnt = signal_strength(cyclecounter, cycle_read_target, mulcnt, signalsum)
    else:
        number = int(command[1])
        cyclecounter, signalsum, cycle_read_target, mulcnt = signal_strength(cyclecounter, cycle_read_target, mulcnt, signalsum)
        cyclecounter, signalsum, cycle_read_target, mulcnt = signal_strength(cyclecounter, cycle_read_target, mulcnt, signalsum)
        register +=number

print(f"Signal strength = {signalsum}")