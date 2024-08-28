a=input()
b=list(a)
p=len(b)
k=p//2
l=0
for i in range (k):
    if b[i]!=b[p-i-1]:
        print(0)
        l+=1
        break
    
if l==0:
    print(1)
        




# string = "hello"
# char_list = []
# for char in string:
#     char_list.append(char)
