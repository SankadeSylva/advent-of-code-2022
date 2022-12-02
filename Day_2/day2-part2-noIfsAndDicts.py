########### Part 2

# A = rock | B = paper | C = scissor
# X = lose | Y = draw | Z = win

hands = ["A", "B", "C", "A", "B"]
results = ["Y", "Z", "X"] #scores: 3,6,0
totScore = 0
with open("day2-data.txt") as game:
    for move in game:
        opponent,result = move.split(" ", 1)
        result = result.strip()
        totScore += (ord(result)-ord("X"))*3 + hands.index(hands[hands.index(opponent)+ results.index(result)])+1 
print(totScore)