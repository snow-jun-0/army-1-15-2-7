# 곡의 개수
# 평균값
# 멜로디 개수

# 멜로디개수 =평균값*곡의 개수
# 멜로디개수의 최소값은 =평균값*곡의개수 -(곡의개수-1)
sing,avg=map(int,input().split())
mel=sing*avg-(sing-1)
print(mel)
