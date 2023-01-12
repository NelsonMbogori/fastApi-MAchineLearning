def last_survivor(letters, coords): 
    chars=[]
    for letter in letters:
        chars.append(letter)
    print(chars)
    for x in range(0,len(coords),1):
        chars.pop(coords[x])
        x += 1
        print(chars)
    return chars.pop()
last_survivor('abcdgfthdd',[1, 2, 3, 4, 5])