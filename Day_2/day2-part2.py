########### Part 2

# Option 1
# A = rock | B = paper | C = scissor
# X = lose | Y = draw | Z = win
hands = ["A", "B", "C"]
winMap = {
    "A" : "B",
    "B" : "C",
    "C" : "A"
}
loseMap = {
    "A" : "C",
    "B" : "A",
    "C" : "B"
}

def getHandScore(hand):
    for i in range(len(hands)):
        if hand == hands[i]:
            return i+1

totScore = 0
with open("day2-data.txt") as game:
    for move in game:
        opponent,result = move.split(" ", 1)
        result = result.strip()
        
        if result == "X":
            totScore += 0 + getHandScore(loseMap[opponent])
        elif result == "Y":
            totScore += 3 + getHandScore(opponent)
        elif result == "Z":
            totScore += 6 + getHandScore(winMap[opponent])

print(totScore)