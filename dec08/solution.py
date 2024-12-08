import numpy as np
import itertools

with open('input_mini', 'r') as f:
    fo = f.readlines()
    fo = np.array([list(f.strip('\n')) for f in fo])
    m = len(fo)
    n = len(fo[0])
#

# day 4 paying dividends!
def in_bounds(_i,_j,m,n):
    return (0<=_i<m) and (0<=_j<n)

def extract_antinodes(pos,_d,_m,_n, maxit=np.inf):
    i,j = pos # assumed the terminal antenna (not start)
    an = []
    i+=_d[0]
    j+=_d[1]
    nit = 0
    while in_bounds(i,j,_m,_n) and nit<maxit:
        an.append( [i,j] )
        i+=_d[0]
        j+=_d[1]
        nit+=1
    an = np.array(an)
    return an

chars = np.setdiff1d(np.unique(fo), ['.'])

################################

# part 1
antinode_maps = {c:np.zeros((m,n), dtype=bool) for c in chars}

for c in chars:
    locs = np.where(fo==c)
    locs = np.reshape(locs,(2,len(locs[1]))).T
    
    for p,q in itertools.combinations(locs, 2):
        an1 = extract_antinodes(q, q-p, m,n, maxit=1)
        an2 = extract_antinodes(p, p-q, m,n, maxit=1)
        # I'm not handling immediate out of bounds cleanly... whatever.
        if len(an1)>0:
            antinode_maps[c][an1[:,0], an1[:,1]] = True
        if len(an2)>0:
            antinode_maps[c][an2[:,0], an2[:,1]] = True

antinodes = np.sum([antinode_maps[c] for c in chars], axis=0, dtype=bool)

print(np.sum(antinodes))

# part 2... do it again.
antinode_maps2 = {c:np.zeros((m,n), dtype=bool) for c in chars}

for c in chars:
    locs = np.where(fo==c)
    locs = np.reshape(locs,(2,len(locs[1]))).T
    
    for p,q in itertools.combinations(locs, 2):
        an1 = extract_antinodes(q, q-p, m,n)
        an2 = extract_antinodes(p, p-q, m,n)
        if len(an1)>0:
            antinode_maps2[c][an1[:,0], an1[:,1]] = True
        if len(an2)>0:
            antinode_maps2[c][an2[:,0], an2[:,1]] = True

# join together the new maps, plus locations of towers themselves.
antinodes2 = [antinode_maps2[c] for c in chars] + [fo!='.']
antinodes2 = np.sum(antinodes2, axis=0, dtype=bool)

print(np.sum(antinodes2))

