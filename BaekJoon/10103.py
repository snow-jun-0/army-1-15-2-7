n=int(input())
ch=100
sd=100
for i in range (n):
    a,b=map(int,input().split())
    if a<b:
        ch-=b
    elif a>b:
        sd-=a

print(ch)
print(sd)
