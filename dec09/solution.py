import numpy as np

with open('input_mini', 'r') as f:
    fo = f.readlines()
    fo = [duh.strip() for duh in fo]
    fo = fo[0]
    _backup = str(fo)

def checksum(_d):
    r=np.where(_d==-1)[0][0]
    return sum((_d>0).astype(np.int64) * np.arange(len(_d), dtype=np.int64)*_d)

# decompress
n=sum([int(z) for z in fo])
_disk = -1*np.ones(n, dtype=np.int64)

# map onto disk
sw=True
p=0
idx=0
for i in range(len(fo)):
    k=int(fo[i])
    if sw:
        _disk[p:p+k]=idx
        idx+=1
        
        sw=not sw
    else:
        sw=not sw
    p+=k
#

# part 1.
disk = np.array(_disk, dtype=np.int64)

r=len(disk)-1
for i in range(len(disk)):
    if disk[i]==-1:
        disk[i]=disk[r]
        disk[r]=-1
        while disk[r]==-1:
            r-=1
    if r<=i:
        break

# part 2.# decompress
n=sum([int(z) for z in fo])
_disk = -1*np.ones(n, dtype=np.int64)

# map onto disk
sw=True
p=0
idx=0
for i in range(len(fo)):
    k=int(fo[i])
    if sw:
        _disk[p:p+k]=idx
        idx+=1
        
        sw=not sw
    else:
        sw=not sw
    p+=k
#
disk = np.array(_disk, dtype=np.int64)
mode=0
contig_l=0
pos_r=len(disk)-1
pos_l=0

boi=disk[pos_r]
while boi>0:

    if mode==0:
        if disk[pos_r]!=boi:
            pos_r-=1
            continue
        # scan right to left for next contig block.
        _id=disk[pos_r]
        br=int(pos_r)+1
        while disk[pos_r]==_id:
            pos_r-=1
        bl=int(pos_r)+1
        fsize=br-bl
        #print('active:', disk[bl:br])
        #print(bl,br)
        mode=1
    if mode==1:
        # scan left to right for an empty block of sufficient size.
        #open_l=contig_l
        #open_r=contig_l
        open_l=0
        open_r=0
        prev=disk[0]
        #import pdb
        #pdb.set_trace()
        for i in range(0,bl): #+1?
            if disk[i]==-1:
                if prev==-1:
                    open_r+=1
                else:
                    open_l=i
                    open_r=i
            else:
                if prev==-1:
                    open_r+=1


            #print(open_l,open_r)
            if open_r-open_l==fsize:
                # yay
                #print('!!',open_l,open_r)
                #print(fsize,bl,br)
                if any(disk[open_l:open_r]!=-1):
                    print(boi,open_l,open_r,disk[bl-1:br+1],disk[open_l:open_r])
                    raise Exception('moo')
                if disk[max(0,open_l-1)]==-1:
                    print(boi,open_l,open_r,disk[bl-1:br+1],disk[open_l:open_r])
                    raise Exception('moo')
                disk[open_l:open_r] = disk[bl:br]
                disk[bl:br] = -1
                break
                
            prev=disk[i]
        mode=0
        boi-=1
    print(boi, bl)
    #print(disk)

if False:
    # Wesley....????
    r=np.where(disk>=0)[0][-1]
    for i in range(len(disk)):
        if disk[i]==-1:
            disk[i]=disk[r]
            disk[r]=-1
            while disk[r]==-1:
                r-=1
        if r<=i:
            break

print(checksum(disk))

