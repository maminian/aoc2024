des = []
updates=[]
with open('input', 'r') as f:
    fo = f.readlines()
    flag=True
    for l in fo:
        if flag:
            c = l.strip().split('|')
            if len(c)==1:
                flag=False # second block
            else:
                des.append(tuple(c[::-1]))
        else:
            c=l.strip().split(',')
            updates.append(c)

# more useful to refer to list of pages you must appear after.
des_d = {}
for i,j in des:
    if i in des_d.keys():
        des_d[i].append(j)
    else:
        des_d[i] = [j]

def is_valid(_update, rules, pp=False):
    for i in range(len(_update)):
        # fetch dependences; dictionary returns empty list if no key.
        que=[_update[j] in rules.get(_update[i], []) for j in range(i+1,len(_update))]
        #print(que)
        if any(que):
            if pp:
                print(_update[i+1:len(_update)])
                print(que)
            return False
    return True

def check_parent(v,edges):
    for j in len(edges):
        if v==edges[j][0]:
            v=edges[j][1]

def middle_page(_update):
    n = len(_update) # assume odd...
    return int(_update[(n-1)//2])

# part 1
s = 0
for up in updates:
    #print(up, end=' ')
    gucci = is_valid(up, des_d)
    #print(gucci)
    if gucci:
        s += middle_page(up)
print(s)

# part 2.
s2=0
for _up in updates:
    
    gucci = is_valid(_up, des_d)
    if not gucci:
        up = list(_up) # copy
        new = []
        sub = {v:k for k,v in des if (k in up and v in up)}
        edges = [pair for pair in des if (pair[0] in up) and (pair[1] in up)]
        
        for _ in range(len(up)):
            curr = [e[1] for e in edges]
            dep=[]
            for c in curr:
                if c not in dep:
                    dep.append(c)
            
            for v in up:
                if v not in dep:
                    new.append(v)
                    to_remove=[k for k in range(len(edges)) if edges[k][0]==v]
                    to_remove.sort(reverse=True)
                    for k in to_remove:
                        edges.pop(k)
                    up.remove(v)
                    
        if not is_valid(up,des_d):
            print(up, is_valid(up,des_d))
            print('moo')
            break
        up = new[::-1]
        s2 += middle_page(up)
    #

#
print(s2)


# goodnight sweet prince
#for _ in range(len(up)):
#    v = up[0]
#    print(v)
#    j=0
#    flag=True
#    while flag:
#        out=sub.get(v,False)
#        if type(out)==str:
#            v=out
#        else:
#            flag=out
#    new.append(v)
#    up.remove(v)
#    print(v)
#    # strip from dictionary
#    bak = dict(sub)
#    for k,val in bak.items():
#        if v==val:
#            sub.pop(k)

