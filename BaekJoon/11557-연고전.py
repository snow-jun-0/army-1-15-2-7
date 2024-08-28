#  계획
# 테스트 케이스 몇개 받고
# 몇개 받은만큼 함수를 호출해서
# 함수 호출 변수에 학교의 개수를 받는다.

# 함수는 
# 호출 받은 학교의 개수만큼 for문을 반복한다
# 이름을 받는 리스트 따로, 값 받는 리스트 따로 만들고
# 값끼리 비교해서 더 큰값이 있는 리스트를 찾고
# 그거와 같은 순서에 있는 이름 리스트에서 출력을 한다. 

def find_school_with_max_value(num_schools):
    names = []  #리스트 이름 지을때 s같은것도 생각하기!!!!
    values = [] 
    
    # 학교의 개수만큼 입력 받기
    for _ in range(num_schools):
        # 입력에서 이름과 값을 분리하여 처리
        name, value = input().split() #입력 받는건 문자열로 받기
        value = int(value)  # 값을 정수형으로 변환
        names.append(name)
        values.append(value)
    
    # 가장 큰 값을 찾기 (for문을 통한 비교는 총 횟수를 알아야 하는데, 이 문제는 모르므로 max함수 이용!!!!)
    max_value = max(values)
    max_index = values.index(max_value) #values.index(x)는 리스트 values에서 값 x가 처음으로 나타나는 인덱스를 반환
    
    # 가장 큰 값을 가진 학교 이름과 값 출력
    print(f"{names[max_index]}") #이 방식!!! 기억하고 쓰자

# 사용자로부터 테스트 케이스 수를 입력받기
num_test_cases = int(input())

# 각 테스트 케이스마다 함수 호출
for _ in range(num_test_cases):
    num_schools = int(input())
    find_school_with_max_value(num_schools)

