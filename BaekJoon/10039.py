# 입력을 다섯번 받는다
# 조건 걸어서 만약 점수가 40 미만이면 40으로 바꾸고 나머지는 스킵
"""for i in range(5):
    num=[int(input())]
    if num[i]<40:
        num[i]=40
avg=sum(num)/len(num)
print(avg)"""

# 앞에 방식대로 하면 리스트가 매번 새로 생성!!!
scores=[]
for i in range(5):
    score=int(input())
    if score<40:
        score=40
    scores.append(score)    
avg=sum(scores)/len(scores)
print(int(avg))
# 변수를 하나 가져와서 그걸 계속 새 값으로 바꾸고 리스트에 넣기!!!
