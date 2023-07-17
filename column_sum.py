n=int(input())
m=int(input())
mat=[]
for i in range(n):
    d=[]
    for j in range(m):
        d.append(int(input()))
    mat.append(d)
result=[]    
for j in range(m):
    sum=0
    for i in range(n):
        sum+=mat[i][j]
    result.append(sum)
print(result) 
