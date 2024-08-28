N=int(input())
for i in range (N):
    r,e,c=map(int,input().split())
    if e==(r+c):    
        print("does not matter")
    elif e<(r+c):
        print("do not advertise")
    else:
        print("advertise")
