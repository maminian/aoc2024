
with open('input_mini', 'r') as f:
    fo = f.readlines()
    fo = fo[0].strip().split(' ')

_backup = list(fo)

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

# part 1
for _ in range(25):
    fo=step(fo)
print(len(fo))

# part 2
# they talk about order... but it really doesn't matter.
# need a "resetting" condition and a storage system.
fo = list(_backup)
counts = {fo[i]:1 for i in range(len(fo))}

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

s2=0
for v in counts.values():
    s2+=v
print(s2)

