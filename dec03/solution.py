# ...cheat with regex?!
# ...no.
# ...but should I?
# no.

_PRINT=True
_USE_DODONT=True # TODO: turn tool into a function and have switches in the input.

with open('input_mini', 'r') as f:
    doh = f.readlines()
    doh = [l.strip('\n') for l in doh]
#

def p(s):
    if _PRINT:
        print(s,end='')
def compare(i,s1,c):
    # length-safe comparison of char to entry in string.
    if i>=len(s1):
        return False
    else:
        return s1[i]==c

# part 1.
# strict pattern (speaking of regex): mult([0-9]{1,3},[0-9]{1,3}).
prefix = 'mul('
suffix = ')'
matches=[]

disabled=False # for don't() and do()
do="do()"
dont="don't()"

for line in doh:
    i=0 # local index for comparison against prefix.
    integer1=0
    integer2=0
    buff = ''
    mode=0
    
    for char in line:
        
        if disabled and _USE_DODONT:
            if i==0:
                p('D-// ')
            # TODO: wrap matcher in a function.
            # direct matching of "do()"... 
            if compare(i,do,char):
                p(char)
                i+=1
                buff+=char
                if buff==do:
                    disabled=False
                    i=0
                    mode=0
                    buff=''
                    p('\n')
            else:
                i=0
                buff=''
                p(char)
                p('\n')
            continue
        #
        
        p(char)
        # TODO: cases
        if mode==0:
            
            # TODO: unhook the conditionals... won't be maintainable.
            # is also completely wrong in general terms (any chimera of the patterns work)
            flag=compare(i,prefix,char)
            if _USE_DODONT:
                flag=flag or compare(i,dont,char)
            if flag: 
                #print('moo')
                i+=1
                buff+=char
                if buff==prefix:
                    buff=''
                    mode=1
                elif _USE_DODONT:
                    if buff==dont:
                        mode=0
                        i=0
                        buff=''
                        disabled=True
                        p('\n')
                #
            else: # reset matcher.
                i=0
                buff=''
                p('\n')
            continue
        #
        
        # checkpoint 1; prefix matched.
        if mode==1:
            k=0 # length of integer
            if char not in '0123456789,':
                i=0
                mode=0
                buff=''
                p('\n')
            elif char==',':
                # store and move to checkpoint 2.
                #print('moo')
                
                mode=2
                integer1=int(buff)
                buff=''
            else: # integer
                
                #print('moo')
                buff+=char # append
                k+=1
                if k==4:
                    mode=0
                    k=0
                    i=0
                    p('\n')
            continue
        #
        
        # checkpoint 2; same as above but watching for right parentheses.
        if mode==2:
            k=0 # length of integer
            if char not in '0123456789)': # TODO: generic suffix.
                i=0
                mode=0
                
                p('\n')
                buff=''
                continue
            elif char==')':
                # store and move to checkpoint 3.
                mode=3
                
                integer2=int(buff)
                buff=''
                i=0
                k=0
            else: # integer
                
                buff+=char # append
                k+=1
                if k==4:
                    i=0
                    mode=0
                    buff=''
                    p('\n')
                    continue
        #
        if mode==3:
            # take action
            matches.append( (integer1,integer2) )
            mode=0
            i=0
            buff=''
            p(' <--yay')
            p('\n')
            continue
        #
    # end "for char in line"
# end "for line in doh"

# End result: list of matches as tuples.
print('\nSum of products:', sum([a*b for a,b in matches]))

