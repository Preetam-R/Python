#find prime numbers
num = int(input("enetr the number:"))

if(num<=1):
    print("the number is not prime number")
    
else:
    for i in range(2, int(num**0.5) + 1):
        if(num % i == 0):
            print("its not the prime number")
            break
        else:
            print("the given number",num,"is prime number")
            


    
        