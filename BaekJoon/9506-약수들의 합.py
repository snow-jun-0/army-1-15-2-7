# 계획
# 일단 while 1을 통해 무한 반복하다가
# 값이 -1일경우 break를 한다.
# 값을 입력받는다 
# 그 값의 약수들을 구한다
# 약수들을 더한다
# 그 값이 입력값과 같으면 입력값과 약수들을 출력한다. 이때는 아마 리스트를 써야될거 같다
# 만약 그 값이 다르면 입력값은 아니다 라고 출력한다.

while 1:
    case_num=int(input())
    all=[]
    if case_num==-1:
        break
    else:
        for i in range(1,case_num):
            if case_num%i==0:
                all.append(i)

        divisors_sum = sum(all)       
        if divisors_sum == case_num:
            # 완전수일 때 약수들의 합을 수식으로 표현
            divisors_str = ' + '.join(map(str, all))
            print(f"{case_num} = {divisors_str}")
        else:
            print(f"{case_num} is NOT perfect.")

#값이 무한반복되서 컴퓨터가 아파지기 전에 ctrl+c를 통해 강제 종료 할 수 있다. 
