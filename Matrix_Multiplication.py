'''MATRIX MULTIPLICATION IN PYTHON                        27-08-2025'''
m1=[[2,1,3],[3,4,5]]                               
m2=[[1,2],[0,1],[4,0]]
res=[[0,0],[0,0]]

# m1=[[1,1,1],[2,2,2]]
# m2=[[2,0,1],[1,1,1],[0,2,1]]
# res=[[0,0,0],[0,0,0]]
for i in range(len(m1)):
    for j in range(len(m2)):    #columns of m2 should be here
        for k in range(len(m2)):
            res[i][j]+=m1[i][k]*m2[k][j]
print(res)
