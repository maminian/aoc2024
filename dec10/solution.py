
import numpy as np
import itertools

with open('input', 'r') as f:
    fo = f.readlines()
    fo = [doh.strip() for doh in fo]
    fo = np.array([[int(fi) for fi in doh] for doh in fo])

def get_nbrs(_map, i,j):
    m,n = np.shape(_map)
    nbrs = [(i,min(n-1,j+1)),(max(0,i-1),j),(i,max(0,j-1)),(min(i+1,m-1),j)]
    nbrs = np.unique(nbrs,axis=0)
    return nbrs
#

def ij2idx(i,j, m=fo.shape[1]):
    return i*m + j
def idx2ij(idx, m=fo.shape[1]):
    return int(idx//m),np.mod(idx,m)

m,n = fo.shape
edgelist = []
trailheads = []
peaks = []
for i,j in itertools.product(range(m), range(n)):
    nb = get_nbrs(fo, i,j)
    # for now: only ascents of exactly 1.
    for p,q in nb:
        if fo[p,q]-fo[i,j] in [1]:
            edgelist.append( (ij2idx(i,j), ij2idx(p,q)) )
    if fo[i,j]==0:
        trailheads.append(ij2idx(i,j))
    if fo[i,j]==9:
        peaks.append(ij2idx(i,j))
#

byvertex={}
for vi,vj in edgelist:
    if vi not in byvertex.keys():
        byvertex[vi] = [vj]
    else:
        byvertex[vi].append(vj)

def moo(idx, use_unique=True):
    paths=byvertex.get(idx,[])
    _i,_j=idx2ij(idx)
    if len(paths)==0:
        if fo[_i,_j]==9:
            return (_i,_j)
        else:
            return None
    else:
        doi = [moo(p,use_unique=use_unique) for p in paths]
        dur = []
        for di in doi:
            if (di is None) or (len(di)==0):
                continue
            dur.append(di)
        doi=dur
        if len(doi)!=0:
            doi = np.vstack(doi)
            if use_unique:
                doi = np.unique(doi, axis=0)
        return doi
#

# part 1
s=0
for t in trailheads:
    duh=moo(t)
    s+=len(duh)

print(s)

# part 2
s=0
for t in trailheads:
    duh=moo(t, use_unique=False)
    s+=len(duh)

print(s)


