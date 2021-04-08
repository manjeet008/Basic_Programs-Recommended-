list=[]
length=int(input("ENTER THE LIST LENGTH... "))
print("ENTER ITEMS IN THE LIST SEPARATED BY COMMA.... ")
for i in range(length):
    list.append(input(f"Enter the {i+1}th item.."))
for count,value in enumerate(list):
    print(count,value)