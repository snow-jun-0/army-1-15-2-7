test=int(input())
i=2
if test==1:
    print("")
while i<=test:
    if test%i==0:
        test=(test/i)
        print(i)
    else:
        i=i+1
