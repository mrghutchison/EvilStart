fp = open("e:\\words.txt","r")
done = False
words = []
while (not done):
    word = fp.readline()
    if (len(word)==0):
        done = True
    else:
        if (len(word)>4):
            words.append(word.strip())

print (len(words))
words.sort()
