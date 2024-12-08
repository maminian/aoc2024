import numpy as np
import itertools

np.random.seed(8122024)

from matplotlib import pyplot as plt
from matplotlib import patches, collections

#there was an approach that didn't require a package...
from pyfonts import load_font
font = load_font(
   font_path="Atkinson-Hyperlegible-Regular-102.otf"
)

#

with open('input', 'r') as f:
    fo = f.readlines()
    fo = np.array([list(f.strip('\n')) for f in fo])
    m = len(fo)
    n = len(fo[0])
#

_PRINT=False
global _FRAME_NUM
global _sw
global cols
_FRAME_NUM=0
_sw=0
cols=['#f33','#3f3']

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

def save_frame(_f, prefix='frames/frame_'):
    global _FRAME_NUM
    _f.savefig(prefix+str(_FRAME_NUM).zfill(4)+'.png')
    print(f'frame {_FRAME_NUM}')
    _FRAME_NUM+=1
    return

#chars = np.setdiff1d(np.unique(fo), ['.'])
chars = np.array(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

#colmap = {c:list(np.random.uniform(0,1,3))+[1] for c in chars}
o = np.random.permutation(len(chars))
colmap = {c:plt.cm.gist_rainbow(o[i]/len(chars)) for i,c in enumerate(chars)}
colmap['.'] = [0,0,0,0]

#################################################

X = np.zeros((*fo.shape, 4))
for i,j in itertools.product(range(X.shape[0]), range(X.shape[1])):
    X[i,j,:] = colmap.get(fo[i,j], [0,0,0,0])

fig,ax = plt.subplots(figsize=(8,8), constrained_layout=True)
fig.set_facecolor('#222')
ax.set_facecolor([0,0,0,0])

im = ax.imshow(np.transpose(X, (1,0,2)), aspect='equal', origin='lower' )


fig.show()
plt.ion()

#plt_txt_arr = [
#    [
#        ax.text(i,j,fo[i][j], ha='left', va='top', font=font, fontsize=10, bbox={'edgecolor':'#333', 'facecolor':'#eee', 'boxstyle':'round', 'linewidth':0.2}) if fo[i][j]!='.' else None
#    for j in range(n)] 
#for i in range(m)]

#for i in range(m):
#    for j in range(n):
#        plt_txt_arr[i][j]._TOUCH=True

ax.set(xlim=[-1,m], ylim=[-1,n])
#ax.invert_yaxis()

ax.set(xticks=[], yticks=[], aspect='equal')


#################################################

antinode_maps = {c:np.zeros((m,n), dtype=bool) for c in chars}

for c in chars:
    locs = np.where(fo==c)
    locs = np.reshape(locs,(2,len(locs[1]))).T
    
    # highlight
    rects = [patches.Rectangle(locs[i]-0.5, 1,1, facecolor=[0,0,0,0], edgecolor='#eee', linewidth=4) for i in range(len(locs))]
    rects = collections.PatchCollection(rects, match_original=True, zorder=1000)
    coll = ax.add_collection(rects)
    
    save_frame(fig)
    
    for p,q in itertools.combinations(locs, 2):
        an1 = extract_antinodes(q, q-p, m,n)
        an2 = extract_antinodes(p, p-q, m,n)
        
        # I'm not handling immediate out of bounds cleanly... whatever.
        if len(an1)>0:
            antinode_maps[c][an1[:,0], an1[:,1]] = True
            _x,_y = p
            _u,_v = q - p
            _po1 = ax.arrow(_x,_y,_u,_v, color=colmap[c], alpha=0.8, lw=5)
            _u,_v = an1[-1] - p
            _po2 = ax.arrow(_x,_y,_u,_v, color=colmap[c], alpha=0.5, lw=3)
            X[an1[:,0], an1[:,1]] = colmap[c]
            
            im.set_data(np.transpose(X, (1,0,2)))
            
            save_frame(fig)
            _po1.remove()
            _po2.remove()
        if len(an2)>0:
            _x,_y = q
            _u,_v = p - q
            _po1 = ax.arrow(_x,_y,_u,_v, color=colmap[c], alpha=0.8, lw=5)
            _u,_v = an2[-1] - q
            _po2 = ax.arrow(_x,_y,_u,_v, color=colmap[c], alpha=0.5, lw=3)
            X[an2[:,0], an2[:,1]] = colmap[c]
            
            im.set_data(np.transpose(X, (1,0,2)))
            
            save_frame(fig)
            _po1.remove()
            _po2.remove()
            
            
    coll.remove()

