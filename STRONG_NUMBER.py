def fact(num):
    if(num==1):
        return(1)
    else:
        return(num*fact(num-1))
while(True):
    user_input=input("\nEnter any number here...")
    n=int(user_input)
    sum=0
    for i in range(len(user_input)):
        rem=n%10
        n=n//10
        sum=sum+fact(rem)
    if(int(user_input)==sum):
        print(f"\nYES! {user_input} is STRONG NUMBER...")
    else:
        print(f"\nNO! {user_input} is not a STRONG NUMBER...")