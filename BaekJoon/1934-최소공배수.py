case=int(input())

def minmax(x_a,x_b):
    a=[]
    b=[]
    ans=x_a*x_b
    i=2
    while i<=x_a:
        if x_a%i==0:
            x_a=(x_a/i)
            a.append(x_a)
        else:
            i=i+1
    while i<=x_b:
        if x_b%i==0:
            x_b=(x_b/i)
            a.append(x_b)
        else:
            i=i+1
    eql=[]
    for item in a:
        if item in b:
            eql.append(item)
    k=len(item)
    for i in range (k):
        p=item[i]
        ans/p

    return ans

for i in range (case):
    a,b=map(int,input().split())
    minmax(a,b)



# 전역 변수 사용: 함수 내에서 input()을 사용하는 것은 좋지 않은 접근입니다.
#  함수에 직접 매개변수를 전달하는 것이 좋습니다.
# 변수 관리: 변수 a와 b가 잘못 사용되고 있습니다.
# 특히, b는 빈 리스트로 유지되어 있으며, 공통된 요소를 찾는 과정이 잘못되어 있습니다
# 나눗셈 오류: ans /= item[i] 부분에서 item이 리스트인데, 이를 직접 나누는 방식은 잘못된 접근입니다.
# 루프 문제: for i in range(len(item)): 부분에서 item이 리스트이기 때문에,
# 이런 방식으로 접근하는 것은 잘못되었습니다.

# GCD 계산: gcd 함수는 유클리드 알고리즘을 사용하여 두 수의 최대 공약수(GCD)를 계산합니다.

# LCM 계산: GCD를 이용하여 최소 공배수(LCM)를 계산합니다. 공식은 다음과 같습니다: 
# lcm(a,b)=a*b/GCD(a,b)

# gpt code
def minmax(x_a, x_b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    g = gcd(x_a, x_b)
    lcm = (x_a * x_b) // g
    
    return lcm

case = int(input())

for _ in range(case):
    a, b = map(int, input().split())
    result = minmax(a, b)
    print(result)



# 함수는 두 정수 a와 b를 입력받습니다.
# 알고리즘:

# while b:: b가 0이 아닐 때까지 반복합니다.
# a, b = b, a % b:
# a % b는 a를 b로 나눈 나머지를 의미합니다.
# a와 b의 값을 갱신합니다. 새로운 a는 현재 b가 되고, 새로운 b는 a를 b로 나눈 나머지가 됩니다.
# 이 과정은 b가 0이 될 때까지 계속됩니다.
# 종료 조건:

# b가 0이 되면 a가 두 수의 최대 공약수(GCD)가 됩니다. 왜냐하면 유클리드 알고리즘에 따르면, 
# 최종적으로 남는 a가 GCD이기 때문입니다.
