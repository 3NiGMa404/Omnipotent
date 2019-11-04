from math import sqrt as s
def calc(p,q):
    d=0
    for i in range(len(p)): d+=(p[i]-q[i])**2
    return s(d)
