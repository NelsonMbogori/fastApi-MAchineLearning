def last_survivors(string):
    letters = []
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in string:
        letters.append(letter)
    for i in range(0,len(letters)-1,1):
        for j in range(i+1,len(letters)-1,1):
            if letters[j] == letters[i]:
                print(alphabet.index(letters[i]))
                letters = list(map(lambda x: x.replace(letters[i],alphabet[alphabet.index(letters[i])+1]), letters))
                print(letters)
            else:
                print('')
        i+= 1
        
            
        
last_survivors('gbgfgf')