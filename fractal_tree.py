from math import sin, cos
from matplotlib import pyplot as plt

branch_length=1

alpha = 0

d=[[0,1,0]]

c0 = [0,0]
c1 = [branch_length*sin(alpha), branch_length*cos(alpha)]

plt.plot(c0,c1)
for i in range(5):
    n=[]
    for j in range(len(d)):
        n.append([d[j][0]+branch_length*sin(d[j][2]-0.2), d[j][1]+branch_length*cos(d[j][2]-0.2), d[j][2]-0.2])
        n.append([d[j][0]+branch_length*sin(d[j][2]+0.2), d[j][1]+branch_length*cos(d[j][2]+0.2), d[j][2]+0.2])
        plt.plot([d[j][0], n[-2][0]],[d[j][1], n[-2][1]])
        plt.plot([d[j][0], n[-1][0]],[d[j][1], n[-1][1]])
    d=n
    branch_length*=0.6
plt.savefig('tree.png')

