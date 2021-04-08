def fib(first,second,n):
    while(first<n):
        print(first,end=" ")
        first,second=second,first+second
    print()
first=int(input("\nEnter the first number...."))
second=int(input("\nEnter the second number...."))
fib(first,second,1000)
