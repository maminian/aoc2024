
import numpy as np
import itertools

with open('input', 'r') as f:
    fo = f.readlines()
    fo = fo[0].strip().split(' ')

_backup = list(fo)


# 0->1
# floor(log_{10}(i)) even -> split to two; one with "first half" of digits;
# other with "second half"
# else, x<-2024*x.
def step(list_in, raw=False):
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
        list_out = np.concatenate(pre_out)
    else:
        list_out = pre_out
    return list_out

def mergesum(d1,d2):
    '''merge two dictionaries assuming values are numerical; adding values of same key.'''
    d=dict(d1)
    for k,v in d2.items():
        if k in d.keys():
            d[k]+=v
        else:
            d[k]=v
    return d

#################

# part 1
for _ in range(25):
    fo=step(fo)
print(len(fo))

# part 2\
# they talk about order... but it really doesn't matter.
# need a "resetting" condition and a storage system.
fo = list(_backup)
counts = {fo[i]:1 for i in range(len(fo))}

memo={}
for u in range(75):
    to_add={}

    for k,num in counts.items():
        # if first time, then document stones created (memoize)
        if k in memo:
            doi=memo[k]
        else:
            doi=step([k])
            memo[k]=doi
        
        # make running tally of new stones created
        for new_stone in doi:
            if new_stone not in to_add.keys():
                to_add[new_stone]=num
            else:
                to_add[new_stone]+=num
        # remove stones "destroyed" (or mapped)
        counts[k]-=num
    
    # update counts with the new lads
    counts=mergesum(counts, to_add)
#

s2=0
for v in counts.values():
    s2+=v
print(s2)

