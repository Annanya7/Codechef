# cook your dish here
T=int(input())
dif=0
for i in range(T):
    X,Y=[int(x) for x in input().split()]
    dif=X-Y
    if X>Y or X==Y:
        print(dif)
    else:
        print("0")