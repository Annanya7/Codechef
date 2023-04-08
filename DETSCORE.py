# cook your dish here
T=int(input())
c=0
for i in range(T):
    X,N=[int(x) for x in input().split()]
    c=X//10
    print(c*N)