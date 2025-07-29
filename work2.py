# data=[[2,3,4],[35,45,45],[2,3]]

# res=[j for i in data for j in i]
# print(res)

data=[20,21,22,23,24,25,26,27,28,29,30]
res=[(i,i**2) if i%2==0 else (i,i**3) for i in data] 
print(res)