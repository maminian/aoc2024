import csv

with open('input', 'r') as f:
    csvr = csv.reader(f, delimiter=' ')
    lines = list(csvr)
lines = [[int(li) for li in l] for l in lines]

# part 1
def check1a(line):
    return all([line[i]>line[i-1] for i in range(1,len(line))])
def check1b(line):
    return all([line[i]<line[i-1] for i in range(1,len(line))])
def check1(line):
    return check1a(line) or check1b(line)

def check2(line):
    return all([abs(line[i]-line[i-1]) in [1,2,3] for i in range(1,len(line))])

def check3(line):
    return check1(line) and check2(line)


print(sum([check3(l) for l in lines]))

# part 2
# welp thought I'd do something sophisticated -- but max length 
# is 8; guess it's a brute force.

def trial(line):
    if check3(line):
        return True
    # go number by number and see if something gets greenlit
    for i in range(len(line)):
        ll = list(line) # copy
        ll.pop(i)
        if check3(ll):
            return True
    return False

print(sum([trial(l) for l in lines]))

