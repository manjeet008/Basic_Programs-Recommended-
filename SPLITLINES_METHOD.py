string="HELLO \nMANJEET SINGH SINGH\nHOW ARE YOU DOING??\nI AM ROBO.."
#SPLIT THIS STRING INTO LIST
LIST1=string.splitlines()
for i in LIST1:
    print(i)
#DISPLAYING LIST WITH INDEX
for count,value in enumerate(LIST1):
    print(count,value)
