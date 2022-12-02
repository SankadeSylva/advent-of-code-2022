# Part 1
calTots = [0]
elf = 0
highest = 0
stockedElf = 0
with open("day1-data.txt") as file:
    for line in file:
        line = line.rstrip()
        if (line != ""):
            calTots[elf] = calTots[elf] + int(line)
        else:
            if (calTots[elf] > highest):
                highest = calTots[elf]
                stockedElf = elf
            elf += 1
            calTots.append(0)
print(highest)

# Part 2
topThreeElves = sorted(calTots, reverse=True)[:3]
topThreeTotal = 0
for tot in topThreeElves:
    topThreeTotal += tot
print(topThreeTotal)
