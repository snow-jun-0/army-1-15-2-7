hour,minute=input().split()
req=input()
hour=int(hour)
minute=int(minute)
req=int(req)
h1=req//60
m1=req%60
hour+=h1
minute+=m1

if minute >=60:
    hour+=minute//60
    minute-=60
if hour>=24:
    hour-=24   

print("%d %d"%(hour,minute))
# 분 단위 먼저 계산하는 것 등 생각할 요소가 많은 문제이다. 
