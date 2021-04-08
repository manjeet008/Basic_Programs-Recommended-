import time
import random
start_time=time.time()
def name_generator(user_name):
    first=("Tandoori","Laal","Prasad","Peepni","Kallu","Mukhiya",
            "Madan","Gopaal","Lallu","Andha","Ramanand","Devi","Sukoon")
    last=("Makkhan","Chandra","Lallan","Prajapati","Kallan","Sookhni",
            "Madaari","Ranjha","Pallu","Rajan","Kishan","Bihaari","YadavLal")
    fname=random.choice(first)
    lname=random.choice(last)
    return(fname,user_name,lname)
while(True):
    UserName=input("\nEnter your name here...")
    FirstName,MiddleName,LastName=name_generator(UserName)
    print("\n Hello",FirstName,MiddleName,LastName)
    end_time=time.time()
    print("\nThis program is executed in {} seconds..".format(end_time-start_time))