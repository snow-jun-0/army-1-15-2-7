N=int(input())
tell=[]
for i in range(N):
    te=int(input())
    tell.append(te)
ncute=tell.count(0)
cute=tell.count(1)
if cute<ncute:
    print("Junhee is not cute!")
elif cute>ncute:
    print("Junhee is cute!")
