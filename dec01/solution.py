with open('input', 'r') as f:
    ll = f.readlines()

l1=[]
l2=[]
for l in ll:
    l = l.split()
    l1.append(int(l[0]))
    l2.append(int(l[1]))

# cheating
l1.sort()
l2.sort()
print(sum([abs(l1[i]-l2[i]) for i in range(len(l1))]))

# part 2 -- since lists are sorted, scan linearly
# and drop when one list or the other is exhausted.
# (similarity score is centered on list 1 but because 
# they're sorted we're done once either list is exhausted)
s=0
k=0
for i in range(len(l1)):
    multiplier=0
    while l2[k]<=l1[i]:
        if l2[k]==l1[i]:
            multiplier += 1
        k+=1
    s+=l1[i]*multiplier
    
    if k==len(l2)-1:
        break

print(s) # solution
