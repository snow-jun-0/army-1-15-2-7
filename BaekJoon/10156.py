K,N,M=map(int,input().split())
mom=0
pr=K*N
if pr>=M:
    mom+=(pr-M)
print(mom)
