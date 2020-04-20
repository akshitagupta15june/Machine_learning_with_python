import numpy
s="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890./,-@#$%^&abcdefghijklmnopqrstuvwxyz"
p=list(s)
k=numpy.random.randint(0,71,6)
password=p[k[0]]+p[k[1]]+p[k[2]]+p[k[3]]+p[k[4]]+p[k[5]]
print(password)