case = int(input())

def hard():
    re, text = input().split()
    re = int(re)
    result = ''
    for char in text:
        result += char * re
    return result

for _ in range(case):
    print(hard())
