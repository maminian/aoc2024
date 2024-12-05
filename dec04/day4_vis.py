import re
from matplotlib import pyplot as plt

#there was an approach that didn't require a package...
from pyfonts import load_font
font = load_font(
   font_path="Atkinson-Hyperlegible-Regular-102.otf"
)

with open('input_mini', 'r') as f:
    fo = f.readlines()
    fo = [list(f.strip('\n')) for f in fo]
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

def p(*s):
    if _PRINT:
        print(*s)

def in_bounds(_i,_j,m,n):
    return (0<=_i<m) and (0<=_j<n)

def extract(array,direction,pos):
    i,j = pos
    _m = len(array)
    _n = len(array[0])
    buff=''
    while in_bounds(i,j,_m,_n):
        buff+=array[i][j]
        i+=d[0]
        j+=d[1]
    return buff
#
def tuples(array,direction,pos):
    i,j = pos
    _m = len(array)
    _n = len(array[0])
    tuptup=[]
    while in_bounds(i,j,_m,_n):
        tuptup.append((i,j))
        i+=d[0]
        j+=d[1]
    return tuptup
#

def save_frame(_f, prefix='frames/frame_'):
    global _FRAME_NUM
    _f.savefig(prefix+str(_FRAME_NUM).zfill(4)+'.png')
    print(f'frame {_FRAME_NUM}')
    _FRAME_NUM+=1
    return

def scan_vis(_arr,_dir,init):
    global _sw
    global cols

    b = extract(_arr, _dir, init)
    pairs = tuples(_arr,_dir,init)
    
    # Highlight active line
    for _p,_q in pairs:
        bbo = plt_txt_arr[_p][_q].get_bbox_patch()
        bbo.set_edgecolor('#ccc')

    save_frame(fig)
    
    mm = po.finditer(b)
    if mm is not None:
        for match in mm:
            for _idx in range(*match.span()):
                _p,_q = pairs[_idx]
                if plt_txt_arr[_p][_q]._TOUCH:
                    plt_txt_arr[_p][_q].set_backgroundcolor(cols[_sw])
                    _sw = 1 - _sw
                    plt_txt_arr[_p][_q]._TOUCH = False
            
    mm = po.finditer(b[::-1])
    if mm is not None:
        for match in mm:
            for _idx in range(*match.span()):
                _reversi = len(b)-_idx-1
                _p,_q = pairs[_reversi]
                if plt_txt_arr[_p][_q]._TOUCH:
                    plt_txt_arr[_p][_q].set_backgroundcolor(cols[_sw])
                    _sw = 1 - _sw
                    plt_txt_arr[_p][_q]._TOUCH = False
    
    save_frame(fig)
    
    # Unhighlight active line.
    for _p,_q in pairs:
        bbo = plt_txt_arr[_p][_q].get_bbox_patch()
        bbo.set_edgecolor('#333')
    return


fig,ax = plt.subplots(figsize=(8,8), constrained_layout=True)
fig.set_facecolor('#222')
ax.set_facecolor([0,0,0,0])

fig.show()

plt_txt_arr = [
    [
        ax.text(i,j,fo[i][j], ha='center', va='center', font=font, fontsize=4, bbox={'edgecolor':'#333', 'facecolor':'#eee', 'boxstyle':'round', 'linewidth':0.2}) 
    for j in range(n)] 
for i in range(m)]

for i in range(m):
    for j in range(n):
        plt_txt_arr[i][j]._TOUCH=True

ax.set(xlim=[-1,m], ylim=[-1,n])
#ax.invert_yaxis()

ax.set(xticks=[], yticks=[], aspect='equal')

#fig.show()

####################################

po = re.compile('XMAS')

for _ in range(2):
    save_frame(fig)

for i in range(m):
    for d in [(-1,1),(0,1),(1,1)]:
        b = extract(fo, d, (i,0))
        scan_vis(fo,d,(i,0))

for j in range(n):
    for d in [(1,0),(1,1)]:
        if d==(1,1) and j==0: # ew
            continue
        b = extract(fo, d, (0,j))
        scan_vis(fo,d,(0,j))


for i in range(1,m):
    for d in [(1,-1)]:
        b = extract(fo, d, (i, n-1))
        scan_vis(fo,d,(i,n-1))


