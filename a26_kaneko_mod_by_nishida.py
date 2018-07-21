from yuji_lib import make_word
import time

def word_count(i,j):
    print(j)
    l1=[]
    w=0
    for m in range(0,len(i)):
        if i[m:m+len(j)]==j:
            w += 1
    return w

"""
x='abababa'
y='aba'
print(word_count(x,y))
"""

start=time.time()
print(word_count(make_word(1_000_000),make_word(5)))
end=time.time()
print(end-start)


