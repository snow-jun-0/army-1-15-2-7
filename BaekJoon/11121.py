# case=input()
# case=int(case)
# a=[]
# b=[]
# for i in range (case):
#     a,b =input().split()
# for i in range(case):
#     print("case #%d : %d" % (i + 1, a[i] + b[i]))

case = int(input())
a = []
b = []

# 각 케이스에 대해 입력받아 리스트에 추가
for i in range(case):
    x, y = input().split()  # 입력받은 값을 x와 y에 저장
    a.append(int(x))  # 정수로 변환 후 리스트에 추가
    b.append(int(y))  # 정수로 변환 후 리스트에 추가

# 결과 출력
for i in range(case):
    print("case #%d: %d" % (i + 1, a[i] + b[i]))


for i in range(int(input())):
  a,b=map(int,input().split())    
  print("Case #%d: %d"%(i+1,a+b))   

#   각 테스트 케이스마다 "Case #x: "를 출력한 다음 -> 이게 조건이어서 한번에 다 출력되면 안되는 거네 ㅠㅠ
