case=int(input())

a=list(input())

p=a.count('A')
k=a.count('B')

if p>k:
    print('A')
elif p==k:
    print('Tie')
else:
    print('B')
