des = []
updates=[]
with open('input_mini', 'r') as f:
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

def is_valid(_update, rules):
    for i in range(len(_update)):
        # fetch dependences; dictionary returns empty list if no key.
        que=[_update[j] in rules.get(_update[i], []) for j in range(i+1,len(_update))]
        #print(que)
        if any(que):
            return False
    return True

# test
if True:
    for up in updates:
        print(up, end=' ')
        print(is_valid(up, des_d))
