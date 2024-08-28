hour,minute,sec=input().split()
req=input()
hour=int(hour)
minute=int(minute)
sec=int(sec)
req=int(req)
sec+=req

if sec>=60:
    minute+=sec//60
    sec-=sec//60*60

if minute >=60:
    hour+=minute//60
    minute-=minute//60*60

if hour>=24:
    hour-=24   

print("%d %d %d"%(hour,minute,sec))

# / 는 나눗셈 즉 값에 따라 실수일 수도, 정수일 수도 있다
# // 는 몫 즉 자연수일 수 밖에 없다.
# % 는 나머지 즉 자연수일 수 밖에 없다. 

# GPT 답안 
hour, minute, sec = map(int, input().split()) #이건 배워야 할 점!!!!
req = int(input())

# 초를 추가하고 처리
sec += req

# 초를 60으로 나누어 분으로 변환
minute += sec // 60
sec = sec % 60

# 분을 60으로 나누어 시간으로 변환
hour += minute // 60
minute = minute % 60

# 시간을 24로 나누어 24시간 형식으로 변환
hour = hour % 24

print(f"{hour} {minute} {sec}")



# D의 최댓값은 50만임으로 
# 약 138시간이 넘습니다 
# 즉

# "디지털 시계는 23시 59분 59초에서 1초가 지나면 0시 0분 0초가 된다."

# 이런 경우가 여러번 발생할수 있습니다.

# 틀린것과 별개로 
# 나머지를 복잡하게 구하셨는데 sec = sec%60 으로 간편하게 구할 수 있습니다.
