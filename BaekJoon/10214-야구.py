T=int(input())
for i in range(T):
    y=[]
    k=[]

for i in range(T):
    for i in range(9):
        a,b=map(int,input().split())
        y.append(a)
        k.append(b)

    re_k=sum(k)
    re_y=sum(y)
    if re_k>re_y:
        print("Korea")
    elif re_k==re_y:
        print("Draw")
    else:
        print("Yonsei")
  

# 리스트 초기화: 각 테스트 케이스에 대해 k와 y 리스트를 새롭게 초기화합니다. 
# 이렇게 해야 각 테스트 케이스가 독립적으로 처리됩니다.


