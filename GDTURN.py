# cook your dish here
T=int(input())
for i in range(T):
    X,Y=[int(x) for x in input().split()]
    if X+Y >6:
        print("YES")
    else:
        print("NO")
    