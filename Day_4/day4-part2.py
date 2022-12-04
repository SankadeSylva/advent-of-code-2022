count = 0
with open("day4-data.txt") as list:
    for pair in map(str.strip, list):
        elf1,elf2 = pair.split(",",1)
        s1,e1 = elf1.split("-",1)
        s2,e2 = elf2.split("-",1)
        elf1 = set(range(int(s1),int(e1)+1))
        elf2 = set(range(int(s2),int(e2)+1))

        if elf1.intersection(elf2):
            count += 1

print(count)