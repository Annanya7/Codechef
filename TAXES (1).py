# cook your dish here
T=int(input())
tax=10
for i in range(T):
    X=int(input())
    if X>100:
        print(X-tax)
    else:
        print(X)