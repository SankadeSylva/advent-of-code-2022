count = 0
with open("day4-data.txt") as list:
    for pair in map(str.strip, list):
        s1, e1, s2, e2 = pair.replace("-", ",").split(",")
        if min(int(e1), int(e2)) >= max(int(s1), int(s2)):
            count += 1

print(count)