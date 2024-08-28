def game():
    money=0
    re1,re2,re3=map(int,(input().split()))
    if(re1 == re2 and re2 == re3):
        money+=10000+(re1*1000)
    elif(re1 == re2 or re2==re3 or re3==re1):
        if(re1==re2):
            money+=1000+(re1*100)
        elif(re2==re3):
            money+=1000+(re2*100)
        else:
            money+=1000+(re3*100)
    else:
        if(re1<re2):
            if(re2<re3):
                money+=100*re3
            else:
                money+=100*re2        
        elif(re1>re3):
            money+=100*re1
        else:
            money+=re3*100
    return money

user=int(input())
li=[]
for i in range(user):
    li.append(game())
li.sort(reverse=True)
print(li[0])


