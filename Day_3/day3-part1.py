doubleItemsAll = []
sum = 0

with open("day3-data.txt") as list:
    for bag in list:
        doubleItemsBag = []
        items = [x for x in bag[:-1]]
        pock1, pock2 = items[:len(items)//2], items[len(items)//2:]

        for item in pock1:
            if item in pock2 and item not in doubleItemsBag:
                doubleItemsBag.append(item)
                doubleItemsAll.append(item)

for x in doubleItemsAll:
    x = ord(x) - 38 - 58 * x.islower()
    sum += x

print(sum)
