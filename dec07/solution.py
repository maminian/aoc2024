import itertools

with open('input', 'r') as f:
    fo = f.readlines()
    fo = [guh.strip().split(' ') for guh in fo]
    fo = [[int(guh[i]) if i!=0 else int(guh[i][:-1]) for i in range(len(guh))] for guh in fo]

def mult(a,b):
    return a*b
def add(a,b):
    return a+b
def concat(a,b):
    return int(str(a)+str(b))

def eval_line(line,ops):
    rest = line[1:]
    s=rest[0]
    for i in range(1,len(rest)):
        s=ops[i-1](s,rest[i])
    return s==line[0]

doi={add:'+',mult:'*',concat='||'}

###############

sum_test = 0
for line in fo:
    _n = len(line)-2
    combos = itertools.product([add,mult], repeat=_n)
    
    for i,c in enumerate(combos):
        if eval_line(line, c):
            sum_test += line[0]
            break

print(sum_test)

################################
# part 2
sum_test = 0
for line in fo:
    _n = len(line)-2
    combos = itertools.product([add,mult,concat], repeat=_n)
    
    for i,c in enumerate(combos):
        if eval_line(line, c):
            sum_test += line[0]
            break

print(sum_test)
