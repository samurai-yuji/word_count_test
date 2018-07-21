from yuji_lib import make_word
import time

def num(lw,sw):
    print(sw)
    beg=0
    cnt=0
    while True:
        idx = lw.find(sw,beg)
        if idx == -1:
            break
        else:
            cnt+=1
            beg=idx+1
    return cnt
           
"""
x='abababa'
y='aba'
print(num(x,y))
"""

start=time.time()
print(num(make_word(1_000_000),make_word(5)))
end=time.time()
print(end-start)


