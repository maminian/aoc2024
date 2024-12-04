import itertools
import numpy as np
import re

with open('input_mini', 'r') as f:
    fo = f.readlines()
    fo = np.array([list(f.strip('\n')) for f in fo])
#

_PRINT=True

def p(*s):
    if _PRINT:
        print(*s)

def in_bounds(_i,_j,m,n):
    return (0<=_i<m) and (0<=_j<n)
def extract(array,direction,pos):
    i,j = pos
    buff=''
    while in_bounds(i,j,*fo.shape):
        buff+=fo[i,j]
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
for _start in starts:
    p("\n",_start,"\n=============")
    for d in do:
        # bypass running in direction parallel to bdry.
        if (d[0]==0 and _start[1] in [0,fo.shape[1]-1]) or (d[1]==0 and _start[0] in [0,fo.shape[0]-1]):
            continue
        b=extract(fo, d, _start)
        count += len(po.findall(b))
        p(d,b,len(po.findall(b)),count)

print(count)

