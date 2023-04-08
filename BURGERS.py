# cook your dish here
T=int(input())
for i in range(T):
    A,B=[int(x) for x in input().split()]
    if A>=1 and B>=1:
        print(min(A,B))