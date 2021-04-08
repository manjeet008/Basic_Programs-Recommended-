result=lambda item : item**2
list=[2,4,6,8,10]
new_list=[]
for i in range(0,len(list)):
  new_list.append(result(list[i]))
print(new_list)