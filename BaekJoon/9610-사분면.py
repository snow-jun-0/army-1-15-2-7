case=int(input())
x=[]
y=[]
Q1=0
Q2=0
Q3=0
Q4=0
AXIS=0
for i in range(case):
    x_,y_=map(int,input().split())
    x.append(x_)
    y.append(y_)

for i in range(case):
    if x[i]>0 and y[i]>0:
        Q1+=1
    elif x[i]>0 and y[i]<0:
        Q4+=1
    elif x[i]<0 and y[i]>0:
        Q2+=1
    elif x[i]<0 and y[i]<0:
        Q3+=1
    else:
        AXIS+=1

print("Q1: %d"%(Q1))
print("Q2: %d"%(Q2))
print("Q3: %d"%(Q3))
print("Q4: %d"%(Q4))
print("AXIS: %d"%(AXIS))
