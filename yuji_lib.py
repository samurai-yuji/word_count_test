import random

def make_word(size):
    words="abc"
    new=[]

    for i in range(0,size):
        i=int(random.random()*3)
        new.append(words[i])

    return "".join(new)

