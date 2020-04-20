
def rotate_left(n,m):
    return n[m:]+n[:m]

def rotate_right(n,m):
    return n[-m:]+n[:-m]
n=[2,5,3,2,6,7,8]
q=rotate_left(n,2)
p=rotate_right(n,2)
print(q)
print(p)


