one=input()
two=input()
one=int(one)
two=int(two)
a=two//100
b=(two-a*100)//10
c=(two-a*100-b*10)
three=one*c
four=one*b
five=one*a
print(three)
print(four)
print(five)
three=one*c
four=one*b*10
five=one*a*100
six=three+four+five
print(six)

# 내 풀이와 비교해 볼거
# A = int(input())
# B = int(input())
# a = A*(B//100)
# b = A*(B//10%10)
# c = A*(B%10)
# print(c)
# print(b)
# print(a)
# print(a*100+b*10+c)


# input이 문자열이라는 것을 이용해서 만든거
# A = int(input())
# B = int(input())
# a = A*(B//100)
# b = A*(B//10%10)
# c = A*(B%10)
# print(c)
# print(b)
# print(a)
# print(a*100+b*10+c)


# / 는 나눗셈 즉 값에 따라 실수일 수도, 정수일 수도 있다
# // 는 몫 즉 정수일 수 밖에 없다.
# % 는 나머지 즉 자연수일 수 밖에 없다. 
