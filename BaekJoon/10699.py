# 모듈이란 여러 변수와 함수를 가지고 있는 집합체로, 
# 크게 표준 모듈과 외부 모듈로 나뉜다.

# 그리고 파이썬은 모듈이라는 기능을 통해 코드를 분리하고 공유하며 일반적으로 모듈을 가져오기 위해서 
# import 구문을 사용한다. 

# · 표준 모듈 : 파이썬에 기본적으로 내장되어 있는 모듈

# · 외부 모듈 : 다른 사람들이 만들어서 공개한 모듈 
# · datetime 모듈은 date(날짜), time(시간)과 관련된 모듈로, 날짜 형식을 만들 때 자주 사용되는 코드들로 구성되어 있다. 

# ​

# · datetime.datetime 은 date 모듈과 time 모듈의 조합으로 
# year(년), month(월), day(일), hour(시),  minute(분), second(초)의 정보를 나타낸다.

import datetime
print(str(datetime.datetime.now())[:10]) # now() 함수를 사용해 지금의 날짜, 시간을 출력

 # str() 함수를 사용해 출력하려는 내용을 string 형태로 출력
 # [:10]를 사용해 10글자만 출력하도록 하여 년, 월, 일만 출력하도록  함  
 


# import datetime

# print(str(datetime.datetime.today())[:10])

# import datetime
# d=datetime.date.today() #오늘 날짜의 date 객체 생성
# print(d.isoformat())  #date 객체의 정보를 'YYYY-MM-DD'형태의 문자열로 반환하는 메서드
