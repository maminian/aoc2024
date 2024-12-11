
import networkx
from matplotlib import pyplot as plt
import numpy as np

global _FRAME_NUM
_FRAME_NUM=0

_VIS_RAW = False

try:
    import cmocean
    if _VIS_RAW:
        mycm = cmocean.cm.dense
    else:
        mycm = cmocean.cm.curl
except:
    if _VIS_RAW:
        mycm = plt.cm.viridis
    else:
        mycm = plt.cm.bwr


_BGCOL = '#eeb'

##################################################################

with open('input_custom', 'r') as f:
    fo = f.readlines()
    fo = fo[0].strip().split(' ')

_backup = list(fo)

def save_frame(_f, prefix='frames/frame_'):
    global _FRAME_NUM
    _f.savefig(prefix+str(_FRAME_NUM).zfill(4)+'.png')
    print(f'frame {_FRAME_NUM}')
    _FRAME_NUM+=1
    return

# 0->1
# floor(log_{10}(i)) even -> split to two; one with "first half" of digits;
# other with "second half"
# else, x<-2024*x.
def step(list_in, raw=False):
    if isinstance(list_in,str):
        list_in=[list_in]
    pre_out = []
    for s in list_in:
        k=len(s)
        if int(s)==0:
            pre_out.append(['1'])
        elif k%2==0:
            pre_out.append([str(int(s[:k//2])), str(int(s[k//2:]))])
        else:
            pre_out.append([str(int(s)*2024)])
    if not raw:
        #list_out = np.concatenate(pre_out)
        list_out = sum(pre_out,[]) # concat lists
    else:
        list_out = pre_out
    return list(list_out)

def mergesum(d1,d2):
    '''Merge two dictionaries assuming values are numerical; adding values of same key.
    returns the new dictionary.'''
    d=dict(d1)
    for k,v in d2.items():
        if k in d.keys():
            d[k]+=v
        else:
            d[k]=v
    return d

def fetch_or_lookup(_func, _memo, _input):
    '''
    Return lookup table result for function input if it exists; else call 
    the function with the input. Dictionary will be updated.
    '''
    if _input in _memo.keys():
        return _memo[_input]
    else:
        _output = _func(_input)
        _memo[_input] = _output
        return _output

#################

counts={fo[i]:1 for i in range(len(_backup))}
memo={}
for _ in range(75):
    to_add={}

    for k,num in counts.items():
        # if first time, then document stones created (memoize)
        new_stones = fetch_or_lookup(step, memo, k)
        
        # make running tally of new stones created
        for ns in new_stones:
            if ns not in to_add.keys():
                to_add[ns]=num
            else:
                to_add[ns]+=num
        
        # remove stones "destroyed" (or mapped)
        counts[k]-=num
    
    # update counts with the new lads
    counts=mergesum(counts, to_add)
#

# second time with full vertex information.
c2 = {k:0 for k in memo.keys()}
c2 = mergesum(c2, {fo[i]:1 for i in range(len(_backup))})

history=[c2]

for _ in range(75):
    to_add={}

    for k,num in c2.items():
        # if first time, then document stones created (memoize)
        new_stones = fetch_or_lookup(step, memo, k)
        
        # make running tally of new stones created
        for ns in new_stones:
            if ns not in to_add.keys():
                to_add[ns]=num
            else:
                to_add[ns]+=num
        
        # remove stones "destroyed" (or mapped)
        c2[k]-=num
    
    # update counts with the new lads
    c2=mergesum(c2, to_add)
    history.append(dict(c2))
#


########################


def logscale(pos_dict):
    X = np.vstack(list(pos_dict.values()))
    xmin,ymin = np.min(X,axis=0)
    po = {k:10**(v-np.array([xmin-0.1, ymin-0.1])) for k,v in pos_dict.items()}
    return po

def draw_graph_state(_G, _state, myax):
    log_sizes = np.array([np.log10(1.1+_state.get(k,0)) for k in _G.nodes])
    
    rel_diff = log_sizes - np.median(log_sizes)
    scale = min(abs(min(rel_diff)), abs(max(rel_diff)))
    
    if _VIS_RAW:
        nodecols = log_sizes/np.max(log_sizes)
        vmin=0
        vmax=1
    else:
        nodecols = rel_diff
        vmin=-scale
        vmax=scale
    
    duh = networkx.draw(
        _G, pos=vpos, ax=myax,
        arrowsize=5, 
        width=0.5,
        #with_labels=True,
        with_labels=False,
        node_size=50 + 100*log_sizes,
        node_color=nodecols,
        cmap=mycm,
        vmin=vmin,
        vmax=vmax,
        #node_color=mycm(rel_diff),
        #edge_color='#222',
        edgecolors='#000'
        )

    for _t in myax.texts:
        _t.set_color('#222')
        _t.set_ha('right')
        _t.set_va('top')
    return
#


G = networkx.DiGraph(memo)
#vpos = networkx.kamada_kawai_layout(G)
vpos = networkx.spectral_layout(G)
#vpos = logscale(vpos)

fig,ax = plt.subplots(figsize=(10,10), constrained_layout=True)
fig.set_facecolor(_BGCOL)

for i in range(len(history)):
    _c = history[i]
    ax.cla()
    
    draw_graph_state(G, _c, ax)

    ax.set_facecolor([0,0,0,0])
    fig.set_facecolor(_BGCOL)
    save_frame(fig)



fig.show()
plt.ion()

