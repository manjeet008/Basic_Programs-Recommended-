#ANOTHER METHOD
def highest_even(li):
    list=[]
    for item in li:
        if (item%2==0):
            list.append(item)
    return(max(list))
print(highest_even([11,2,5,67,50,99]))