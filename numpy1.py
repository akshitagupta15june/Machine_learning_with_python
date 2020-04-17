import numpy as np
from numpy.linalg import *
x=np.array([4,6,8,9])
#4x-6y=20
#3x+7y=25
y=np.array([[4,-6],[3,7]])
z=np.array([[18],[25]])
print(np.linalg.solve(y,z))
g=np.arange(10)
print(g)
h=np.arange(5,10)
print(h)
s=np.arange(2,10,2)
print(s)
p=np.linspace(2,12,5)
print(p)
n=np.zeros((2,5))
print(n)
m=np.ones((2,5))
print(m)
e=np.eye(3)
print(e)
