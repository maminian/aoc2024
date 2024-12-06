
import numpy as np

with open('input', 'r') as f:
    fo = f.readlines()
    fo = np.array([list(q.strip()) for q in fo])
    m,n = fo.shape


def in_bounds(_i,_j,m,n):
    return (0<=_i<m) and (0<=_j<n)


walked = np.zeros((m,n), dtype=bool)
i,j = np.where((fo != '.') & (fo != '#'))
i0=i[0]
j0=j[0]

i,j=int(i0),int(j0) # copy
d=(-1,0)

#

rt={(0,1):(1,0), (1,0):(0,-1), (0,-1):(-1,0), (-1,0):(0,1)}

steps=0
while in_bounds(i,j,m,n):
    walked[i,j]=True
    
    _p,_q=(i+d[0], j+d[1])
    if not in_bounds(_p,_q,m,n):
        break
    if fo[_p,_q]=='#':
        d = rt[d] # right turn!
        continue

    i,j = (_p,_q)
    steps += 1

# Part 2: insert obstruction for periodic behavior.
# Basic observation: obstruction will force a path which *leads*
# the guard onto a prior path which goes in the *same* direction.
# walked2 = np.zeros((4,m,n), dtype=bool)
# k={(-1,0):0, (0,1):1, (1,0):2, (0,-1):3}

i,j=int(i0),int(j0) # copy
d=(-1,0)


def does_it_loop(o_i,o_j, doh, maxit=m*n):
    # brute force; lord forgive me.
    mapp = np.array(doh)
    mapp[o_i,o_j] = '#'
    
    i,j=int(i0),int(j0) # copy
    d=(-1,0)
    steps=0
    while in_bounds(i,j,m,n):
        #walked2[k[d], i,j]=True
        
        _p,_q=(i+d[0], j+d[1])
        if not in_bounds(_p,_q,m,n):
            break
        if mapp[_p,_q]=='#':
            d = rt[d] # right turn!
            continue

        i,j = (_p,_q)
        steps += 1
        if steps==maxit:
            return 1
    return 0 # doesn't loop
#

loopcount = 0
for p in range(m):
    for q in range(n):
        if fo[p,q]=='#' or (p,q)==(i0,j0):
            continue
        # number of steps naively bounded by 2mn if not looping?
        # Thinking: if +1, then a square was visited three times;
        # either passed through in the same direction twice (implies loop)
        # or passed in three independent directions (not possible...?)
        loopcount += does_it_loop(p,q, fo, m*n*2)
    print(p+1,m)

print(loopcount)
