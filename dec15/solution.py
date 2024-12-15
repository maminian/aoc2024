import itertools
import numpy as np

with open('input_mini3', 'r') as f:
    fo = f.readlines()
    #fo = [list(fi.strip()) for fi in fo])
    w = []
    instr = []
    flag=False
    for line in fo:
        if flag:
            instr.append(list(line.strip()))
        else:
            if len(line[0].strip())==0:
                flag=True
                continue
            w.append(list(line.strip()))
    instr = sum(instr,[])
    w = np.array(w)
#    print(line)
#    _ = input()
print(w)

_card={'<':np.array([0,-1], dtype=int), 
       '^':np.array([-1,0], dtype=int), 
       'v':np.array([1, 0], dtype=int), 
       '>':np.array([0, 1], dtype=int)}

#################

global blob
blob = {}

def p(thing,forreallyreal=False):
    if forreallyreal:
        print(thing)

def move(_map, pos, dir, verb=False):
    global blob

    m,n = _map.shape
    _tmp = _map[tuple(pos)]
    proposed = pos + _card[dir]
    # walk into 
    if _map[tuple(proposed)]=='#':
        p(_map,verb)
        return _map,pos
    if _map[tuple(proposed)]=='.':
        _map[tuple(pos)]='.'
        _map[tuple(proposed)]=_tmp
        p(_map,verb)
        return _map,proposed
    # otherwise, a crate.
    if _map[tuple(proposed)]=='O':
        _map,other = move(_map, proposed, dir)
        if tuple(other) == tuple(proposed): # didn't move!
            p(_map,verb)
            return _map,pos
        else:
            _map[tuple(pos)]='.'
            _map[tuple(proposed)]=_tmp
            p(_map,verb)
            return _map,proposed
    # part 2...
    if dir in '<>': # left or right can fall back to previous rules
        _map,other = move(_map, proposed, dir)
        if tuple(other) == tuple(proposed): # didn't move!
            p(_map,verb)
            return _map,pos
        else:
            _map[tuple(pos)]='.'
            _map[tuple(proposed)]=_tmp
            p(_map,verb)
            return _map,proposed
    else:
        # up/down: need to:
        # (a) check rules for both "left half" and "right half" of box;
        # (b) ensure properly following recursive chain of dependencies.
        bros = [proposed]
        if _map[tuple(proposed)]=='[':
            bros.append(tuple(proposed+np.array([0,1])))
        else:
            bros.append(tuple(proposed+np.array([0,-1])))
        bros_ok = [check_only(_map,b,dir) for b in bros]
        if all(bros_ok):
            _new = _map.copy()
            #import pdb
            #pdb.set_trace()
            for k in blob.keys():
                loc = np.array(k) + _card[dir]
                _new[tuple(loc)] = _map[k]

                _new[k] = _map[tuple(np.array(k) - _card[dir])] #hrm
            p(_new,verb)
            blob = {tuple(proposed):True}
            return _new, proposed
        else:
            # abort abort
            p(_map,verb)
            blob = {tuple(pos):True}
            return _map,pos
#

def check_only(_map,pos,dir,recurse=True):
    global blob
    
    _tmp = _map[tuple(pos)]
    proposed = pos + _card[dir]
    char=_map[tuple(proposed)]
    
    if recurse:
        if _tmp=='[':
            #import pdb
            #pdb.set_trace()
            nbr=pos+np.array([0,1])
            works2=check_only(_map,nbr,dir,recurse=False)
        elif _tmp==']':
            nbr=pos+np.array([0,-1])
            works2=check_only(_map,nbr,dir,recurse=False)
        else:
            works2=True
    else:
        works2=True
    
    if char=='#':
        return False
    elif char=='.':
        works=True
    else:
        works=check_only(_map,proposed,dir)

    blob[tuple(pos)] = works and works2 and blob.get(tuple(pos), True)
    return works

def get_GPS(pos):
    return 100*pos[0] + pos[1]

def get_map_GPS(_map):
    locs = np.where(_map=='O')
    s = 0
    for i in range(len(locs[0])):
        s += get_GPS((locs[0][i], locs[1][i]))
    return s
    
##

def expand_map(_map, _r={'#':'##', 'O':'[]', '.':'..', '@':'@.'}):
    m,n = _map.shape
    new = []
    for row in _map:
        st = ''
        for e in row:
            st = st + _r[e]
        newrow = list(st)
        new.append(newrow)
    return np.array(new)

##

w2 = expand_map(w)

########

# part 1
pos = np.concatenate(np.where(w=='@'))
for i in range(len(instr)):
    #p(i,r'\n')
    #p(w,True)
    
    w,pos =  move(w, pos, instr[i], False)
#

print( get_map_GPS(w) )

##
# part 2
pos = np.concatenate(np.where(w2=='@'))
blob[tuple(pos)]=True
for i in range(len(instr)):
    p(i,r'\n')
    #p(w,True)
    
    w2,pos =  move(w2, pos, instr[i], True)
#



