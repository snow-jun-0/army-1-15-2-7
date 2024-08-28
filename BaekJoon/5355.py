# 내 코드
# test=int(input())
# for i in range (test):
#     a = list(map(str,input().split()))
#     a[0]=float(a[0])
#     if a[i]=='@':
#         a[0]*=3
#     if a[i]=='#':
#         a[0]-=7
#     if a[i]=='%':
#         a[0]+=5
#     print("%0.2f" % a[0])


# gpt 코드
test = int(input())

for _ in range(test):
    # 화성 수학식을 입력받고 공백으로 분리
    parts = input().split()  #그냥 여러값을 한 변수에 넣으면 그건 리스트가 된다. 
    # 첫 번째 요소는 수, 나머지는 연산자
    number = float(parts[0])
    operators = parts[1:]

    # 연산자 순서대로 적용
    for op in operators:
        if op == '@':
            number *= 3
        elif op == '#':
            number -= 7
        elif op == '%':
            number += 5

    # 결과를 소수점 둘째 자리까지 출력
    print(f"{number:.2f}")
    print("%0.2f" % number)




# case = int(input())

# for _ in range(case):
#     mars = list(map(str, input().split()))
#     answer = 0
#     for i in range(len(mars)):
#         if i == 0:
#             answer += float(mars[i])
#         else:
#             if mars[i] == "#":
#                 answer -= 7
#             elif mars[i] == "%":
#                 answer += 5
#             elif mars[i] == "@":
#                 answer *= 3
                
#     print("%0.2f" % answer)
