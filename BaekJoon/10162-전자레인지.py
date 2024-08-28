T=int(input())
A=300
B=60
C=10

if T<=60:
    if T%10!=0:
        print(-1)
    elif T==60:
        print("%d %d %d"%(0,1,0))
    else:
        k=T//C
        print("%d %d %d"%(0,0,k))
elif T<=300:
    if T%10!=0:
        print(-1)
    elif T==300:
        print("%d %d %d"%(1,0,0))
    else:
        k=T//B
        l=(T%B)//C   
        print("%d %d %d"%(0,k,l))
elif T<=10000:
    if T%10!=0:
        print(-1)
    else:
        k=T//A
        l=(T%A)//B
        m=(T%A)%B//C
        print("%d %d %d"%(k,l,m))
