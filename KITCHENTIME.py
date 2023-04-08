# cook your dish here
T=int(input())
for i in range(T):
    X,Y=[int(x) for x in input().split()]
    print(abs(X-Y))