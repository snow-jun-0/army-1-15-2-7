# x=[]
# y=[]
# for i in range (3):
#     x,y=map(int,input().split())
# if x.count(x[0])==1:
#     r_x=x[0]
# elif x.count(x[1])==1:
#     r_x=x[1]
# else:
#     r_x=x[2]

# if y.count(y[0])==1:
#     r_y=y[0]
# elif y.count(y[1])==1:
#     r_y=y[1]
# else:
#     r_y=y[2]

# print("%d %d"%(r_x,r_y))

# !!!!내가 또 한 실수!!! 리스트를 직접 사용하는게 아니라 다른 변수를 만들고 그 변수 값을 리스트에 넣어야 하는데 ㅠㅠ

x = []
y = []

# 입력값을 리스트에 저장
for _ in range(3):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

# x 리스트에서 유일한 값 찾기
if x.count(x[0]) == 1:
    r_x = x[0]
elif x.count(x[1]) == 1:
    r_x = x[1]
else:
    r_x = x[2]

# y 리스트에서 유일한 값 찾기
if y.count(y[0]) == 1:
    r_y = y[0]
elif y.count(y[1]) == 1:
    r_y = y[1]
else:
    r_y = y[2]

# 결과 출력
print(f"{r_x} {r_y}")
