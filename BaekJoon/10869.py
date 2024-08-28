a,b=input().split()
a=int(a)
b=int(b)
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)

#split 함수
#문자열.split("특정 문자")의 구조로 사용합니다.
#문자열의 특정 문자를 기준으로 나눠줍니다.(특정 문자는 삭제됩니다.)

#input 메서드
#input 함수를 사용하여 입력 받은 값은 항상 문자열 형식으로 반환된다. 
#그래서 num = int(input("정수를 입력하세요 : ")) 이런 형식으로 사용한다. 

# 연산자
# / 는 나눗셈 즉 값에 따라 실수일 수도, 정수일 수도 있다
# // 는 몫 즉 자연수일 수 밖에 없다.
# % 는 나머지 즉 자연수일 수 밖에 없다. 
# ** 는 거듭제곱을 의미하며 숫자1**숫자2 를 통해 숫자1을 숫자2만큼 거듭제곱한다. 

# map 함수
# map(function, iterable)
# function은 각 요소에 적용될 함수이고
# iterable은 함수를 적용할 데이터 집합이다. 
# 즉 map() 함수는 iterable의 각 요소에 대해 function 함수를 적용한 결과를 새로운 iterator로 반환한다

# ex)
# def square(x):  함수 square를 정의한다. 
#     return x**2  이 함수에서는 값을 등록하면 2제곱해서 돌려준다. 

# numbers = [1, 2, 3, 4, 5]  numbers라는 리스트를 만들었다. 
# squared_numbers = map(square, numbers) squared_numbers에 map 함수를 이용해 각 데이터에 square를 적용한다. 
# print(list(squared_numbers))   리스트를 통해 값을 출력해보면 [1, 4, 9, 16, 25] 나온다. 

# ex2)
# a, b, c = map(int, input().split())  // 
# print((a+b)%c, ((a%c) + (b%c))%c, (a*b)%c, ((a%c) * (b%c))%c, sep='\n')
