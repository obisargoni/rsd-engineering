from math import sin, cos
from matplotlib import pyplot as plt
from .branch import Branch

branch_length=1

alpha = 0

d=[[0,1,alpha]]

c0 = [0,0]
c1 = [branch_length*sin(alpha), branch_length*cos(alpha)]

# Initialise first branch
first_branch = Branch(c0, branch_length, alpha)

plt.plot(c0,c1)
for i in range(5):
    n=[]
    for j in range(len(d)):
        aMinus = d[j][2] - 0.2
        aPlus = d[j][2] + 0.2
        
        cDJ = d[j][0:2]
        
        # get two new coordinates based on the previous coordinates
        cMinus = [cDJ[0]+branch_length*sin(aMinus), cDJ[1]+branch_length*cos(aMinus)]
        n.append(cMinus + [aMinus])
        
        cPlus = [cDJ[0]+branch_length*sin(aPlus), cDJ[1]+branch_length*cos(aPlus)]
        n.append(cPlus + [aPlus])
        
        plt.plot([d[j][0], n[-2][0]],[d[j][1], n[-2][1]])
        plt.plot([d[j][0], n[-1][0]],[d[j][1], n[-1][1]])
    d=n
    branch_length*=0.6
plt.savefig('tree.png')

