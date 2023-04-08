# cook your dish here
T=int(input())
for i in range(T):
    X,Y=[int(x) for x in input().split()]
    if X>Y:
        print("LOSS")
    elif Y>X:
        print("PROFIT")
    else:
        print("NEUTRAL")