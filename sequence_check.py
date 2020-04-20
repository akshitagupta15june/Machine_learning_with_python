x=[1,2,3,5,7,1,3]
n=len(x)
k=0
for i in range(n):
    if x[i]==1 and x[i+1]==2 and x[i+2]==3:
        k=1
        print(True)

if(k!=1):
    print(False)