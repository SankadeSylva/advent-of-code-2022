sum = 0
with open("day3-data.txt") as list:
    for bag in map(str.strip, list):
        doubleItem = (set(bag) & set(next(list)) & set(next(list))).pop()
        sum += ord(doubleItem) - 38 - 58 * doubleItem.islower()
print(sum)