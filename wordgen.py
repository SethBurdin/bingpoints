import os
import random



with open('dict.txt') as f:
    lines = f.readlines()
    #lines.translate("\r\n") 
UpperLimit = len(lines)



def randomer():
    i = 0
    randomWord = [0, 1, 2]
    while i < 3:
        picker = random.randrange(0, UpperLimit)
        randomWord[i] = lines[picker].strip()
        i += 1
    searchTerm = randomWord[0] + " " + randomWord[1] + " " + randomWord[2]
    #print(searchTerm)    
    return searchTerm

randomer()