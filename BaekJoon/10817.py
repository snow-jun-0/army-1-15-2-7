A,B,C=map(int,input().split())
lank=[]
lank.append(A)
lank.append(B)
lank.append(C)
lank.sort()
print(lank[1])

a=list(map(int,input().split())) # 앞에 list만 쓰면 되는거였는데 까비
a.sort()
print(a[1])
