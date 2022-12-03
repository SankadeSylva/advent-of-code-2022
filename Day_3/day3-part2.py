doubleItemsAll = []
sum = 0
elves = 1
GroupItems = []
with open("day3-data.txt") as list:
    for bag in list:
        doubleItemsGroup = []
        items = [x for x in bag[:-1]]
        GroupItems.append(items)
        if elves == 3:
            for item in GroupItems[0]:
                if item in GroupItems[1] and item in GroupItems[2] and item not in doubleItemsGroup:
                    doubleItemsGroup.append(item)
                    doubleItemsAll.append(item)
            GroupItems = []
            elves = 0
        elves += 1

for x in doubleItemsAll:
    x = ord(x) - 38 - 58 * x.islower()
    sum += x

print(sum)
