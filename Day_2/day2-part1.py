############ Part 1
# A,X = rock | B,Y = paper | C,Z = scissor
hands = ["X", "Y", "Z"]
handsMap = {
    "X" : "A",
    "Y" : "B",
    "Z" : "C"
}
beatsMap = {
    "A" : "Y",
    "B" : "Z",
    "C" : "X"
}

def getHandScore(hand):
    for i in range(len(hands)):
        if hand == hands[i]:
            return i+1

totScore = 0
with open("day2-data.txt") as game:
    for move in game:
        opponent,me = move.split(" ", 1)
        me = me.strip()
        totScore += getHandScore(me)
        if opponent == handsMap[me]:
            totScore += 3
        elif me == beatsMap[opponent]:
            totScore += 6

print(totScore)