with open("day6-data.txt") as stream:
    line = stream.read()
    for i in range(0, len(line)-14): 
        if len(set(line[i:i+14]))==14: 
            print(i+14) 
            break