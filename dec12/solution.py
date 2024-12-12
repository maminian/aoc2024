import itertools
import numpy as np

with open('input', 'r') as f:
    fo = f.readlines()
    fo = np.array([list(fi.strip()) for fi in fo])

def get_nbrs(i,j,m,n):
#    m,n = np.shape(_map)
    nbrs = [(i,min(n-1,j+1)),(max(0,i-1),j),(i,max(0,j-1)),(min(i+1,m-1),j)]
    nbrs = np.unique(nbrs,axis=0)
    return nbrs
#

def forward_label(_map,_plots,i,j,_label):
    m,n = _map.shape
    if (i,j) in _plots:
        return
    _plots[(i,j)]=_label
    
    nb = get_nbrs(i,j,m,n)
    for b in nb:
        if _map[b[0],b[1]]==_map[i,j]:
            forward_label(_map,_plots,b[0],b[1],_label)
    return

def dict2arr(_d,_a):
    for k,v in _d.items():
        _a[k[0],k[1]]=v
    return _a

def plot_area(_plots,_p):
    return len(_plots[_p])

def plot_perimeter(_map,_plots,_p):
    plot=_plots[_p]
    count=0
    m,n = _map.shape
    for k in plot:
        count+=sum([ki in [0,m-1] for ki in k]) # cheating -- more annoying with non-square.
        #    count+=1
        #    continue
        nb = get_nbrs(k[0],k[1],m,n)
        #import pdb
        #pdb.set_trace()
        que=[tuple(b) not in plot for b in nb]
        #if any(que):
        #    count+=1
        count+=sum(que)
    return count
#

def plot_num_sides(_map,_plots,_p):
    # work counterclockwise around the perimeter and fetch the 
    # number of times the normal vector changes.

def price(_map,_plots,_p):
    return plot_area(_plots,_p)*plot_perimeter(_map,_plots,_p)

def price_all(_map,_plots):
    return sum([price(_map,_plots,_p) for _p in _plots.keys()])

#######################

_backup = list(fo)
m,n = fo.shape

plant_labels = {}

label = -1*np.ones((m,n), dtype=int)

idx=0
for i,j in itertools.product(range(m),range(n)):
    if (i,j) not in plant_labels:
        # label and feed-forward.
        forward_label(fo, plant_labels, i,j, idx)
        idx+=1
#

plots={z:[] for z in range(idx)}
for k,v in plant_labels.items():
    plots[v].append(k)

#

# part 1
print(price_all(fo, plots))

# part 2
# is a VEF format necessary..?
# holding right hand on wall based on pixel regions fails when 
# the region isn't convex, I think.
ex = plots[0]
pos = ex[0]
history = []

