def test(case):
    sol=[]
    for i in range (len(case)):
        sol.append(case[i])

    k=[1]*len(sol)
    for i in range (len(case)):
        if sol[i]=='x':
            k[i]=0

    for i in range (len(case)-1):
        if sol[i]!='x' and sol[i]==sol[i+1]:
            k[i+1]+=k[i]+1
    result=sum(k)
    return result

f=int(input())
for i in range (f):
    a=input()
    test(a)




#gpt
# 테스트 케이스의 개수를 입력받습니다.
num_cases = int(input().strip())

# 각 테스트 케이스를 처리합니다.
for _ in range(num_cases):
    # OX퀴즈 결과를 입력받습니다.
    result = input().strip()
    
    # 점수를 계산하기 위한 변수들입니다.
    score = 0
    current_streak = 0
    
    # 문자열을 순회하면서 점수를 계산합니다.
    for char in result:
        if char == 'O':
            current_streak += 1  # 연속된 'O'의 개수를 증가시킵니다.
            score += current_streak  # 현재까지의 연속된 'O' 개수만큼 점수를 증가시킵니다.
        else:
            current_streak = 0  # 'X'를 만나면 연속 카운트를 초기화합니다.
    
    # 계산된 점수를 출력합니다.
    print(score)


def test(case):
    # 점수와 현재 연속된 O의 개수를 저장할 변수
    score = 0
    current_streak = 0
    
    # 문자열을 순회하면서 점수를 계산
    for char in case:
        if char == 'O':
            current_streak += 1
            score += current_streak
        else:
            current_streak = 0
    
    return score

# 테스트 케이스의 개수를 입력받습니다.
f = int(input().strip())

# 각 테스트 케이스를 처리합니다.
for i in range(f):
    a = input().strip()  # OX퀴즈 결과를 입력받습니다.
    result = test(a)  # 점수를 계산합니다.
    print(result)  # 결과를 출력합니다.
