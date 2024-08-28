def grade(x):
    if x == 4.3:
        x="A+"
    elif x == 4.0:
        x="A0"
    elif x == 3.7:
        x="A-"
    elif x == 3.3:
        x="B+"
    elif x == 3.0:
        x="B0"
    elif x == 2.7:
        x="B-"
    elif x == 2.3:
        x="C+"
    elif x == 2.0:
        x="C0"
    elif x == 1.7:
        x="C-"
    elif x == 1.3:
        x="D+"
    elif x == 1.0:
        x="D0"
    elif x == 0.7:
        x="D-"
    elif x == 0.0:
        x="F"
    return x

i=float(input())
print(grade(i))
# 바보같이 거꾸로 문제 만듬 ㅋㅋ 아 보통 성적은 점수로 나오는게 정배 아니냐고~


def grade(x):
    if x == "A+":
        x=4.3
    elif x == "A0":
        x=4.0
    elif x == "A-":
        x=3.7
    elif x == "B+":
        x=3.3
    elif x == "B0":
        x=3.0
    elif x == "B-":
        x=2.7
    elif x == "C+":
        x=2.3
    elif x == "C0":
        x=2.0
    elif x == "C-":
        x=1.7
    elif x == "D+":
        x=1.3
    elif x == "D0":
        x=1.0
    elif x == "D-":
        x=0.7
    elif x == "F":
        x=0.0
    return x

i=input()
print(grade(i))


