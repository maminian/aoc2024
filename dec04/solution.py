import itertools
import numpy as np
import re

with open('input_mini', 'r') as f:
    fo = f.readlines()
    fo = np.array([list(f.strip('\n')) for f in fo])
#

_PRINT=False

def p(*s):
    if _PRINT:
        print(*s)

def in_bounds(_i,_j,m,n):
    return (0<=_i<m) and (0<=_j<n)
def extract(array,direction,pos):
    i,j = pos
    buff=''
    while in_bounds(i,j,*array.shape):
        buff+=array[i,j]
        i+=d[0]
        j+=d[1]
    return buff
#

# part 1
po = re.compile('XMAS')

# boundaries
starts = list(itertools.product(range(fo.shape[0]-1),[0]))
starts = starts + list(itertools.product([fo.shape[0]-1],range(fo.shape[1])))
starts = starts + list(itertools.product(range(fo.shape[0]-1),[fo.shape[1]-1]))

starts = starts + list(itertools.product([0],range(fo.shape[1]-1)))


#starts = [(9,3)]

# scan directions
do = itertools.product([-1,0,1], [-1,0,1])
do = list(do)
do.remove((0,0))

count=0

for i in range(fo.shape[0]):
    for d in [(-1,1),(0,1),(1,1)]:
        b = extract(fo, d, (i,0))
        count += len(po.findall(b))
        count += len(po.findall(b[::-1]))
        p(d,b,len(po.findall(b)),count)
for j in range(fo.shape[1]):
    for d in [(1,0),(1,1)]:
        if d==(1,1) and j==0:
            continue
        b = extract(fo, d, (0,j))
        count += len(po.findall(b))
        count += len(po.findall(b[::-1]))
        p(d,b,len(po.findall(b)),count)
for i in range(1,fo.shape[0]):
    for d in [(1,-1)]:
        b = extract(fo, d, (i, fo.shape[1]-1))
        count += len(po.findall(b))
        count += len(po.findall(b[::-1]))
        p(d,b,len(po.findall(b)),count)
print(count)

# Part 2
mo = re.compile('MAS')
count2 = 0
for i in range(1,fo.shape[0]-1):
    for j in range(1,fo.shape[1]-1):
        if fo[i,j]!='A': continue
        
        s1 = ''.join([fo[i+k,j+k] for k in range(-1,2)])
        s2 = ''.join([fo[i-k,j+k] for k in range(-1,2)])
        if (mo.match(s1) or mo.match(s1[::-1])) and (mo.match(s2) or mo.match(s2[::-1])):
            count2 += 1
print(count2)


