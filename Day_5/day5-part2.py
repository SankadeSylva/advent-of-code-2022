stacks = [["D","M","S","Z","R","F","W","N"], ["W","P","Q","G","S"], 
["W","R","V","Q","F","N","J","C"], ["F","Z","P","C","G","D","L"], ["T","P","S"], 
["H","D","F","W","R","L"], ["Z","N","D","C"], ["W","N","R","F","V","S","J","Q"], 
["R","M","S","G","Z","W","V"]]

with open("day5-moves.txt") as instructions:
    for line in instructions:
        moves = [int(x) for x in line.split() if x.isdigit()]
        stack = stacks[moves[1]-1]

        for crate in stack[slice(len(stack)-moves[0], len(stack))]:
            stacks[moves[2]-1].append(crate)
            stacks[moves[1]-1].pop()
    
    topCrates = ""
    for stack in stacks:
            topCrates += str(stack.pop())

print(topCrates)