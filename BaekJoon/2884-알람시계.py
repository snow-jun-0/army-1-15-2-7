hour,minute=input().split()
hour=int(hour)
minute=int(minute)
minute-=45

if minute <0:
    hour-=1
    minute=60+minute
if hour<0:
    hour+=24   

print("%d %d"%(hour,minute))
