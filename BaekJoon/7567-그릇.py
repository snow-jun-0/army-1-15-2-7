sol=[]
case=input()
for i in range (len(case)):
    sol.append(case[i])

k=[10]*len(sol)
for i in range (len(case)-1):
    if sol[i]==sol[i+1]:
        k[i+1]=5
    else:
        k[i+1]=10

result=sum(k) #sum(리스트)는 리스트 요소 의 합 내가 푼것도 맞은거임 !!! 케이스 안에 값이 있어야지만
# 값을 =을 이용해서 수정할 수 있음 그래서 리스트 초기화 과정(값이 들어가있는 상황)이 필요함


print(result)

# # 문자열 입력 처리
# case = input().strip()  # 입력 문자열

# sol = list(case)  # 문자열을 리스트로 변환

# # k 리스트 초기화
# k = [10] * len(sol)  # k의 크기를 sol과 동일하게 초기화

# # 인접한 값 비교
# for i in range(len(sol) - 1):  # 마지막 요소를 제외한 범위
#     if sol[i] == sol[i + 1]:
#         k[i + 1] = 5
#     else:
#         k[i + 1] = 10

# # 결과 계산
# result = sum(k)  # 리스트 요소의 합

# print(result)
