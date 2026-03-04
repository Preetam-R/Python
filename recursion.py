#recursion
def show(n):    #this is recursive function
    if(n==0):  #this is base case -- means condition to stop the recursive function 
        return
    print(n)
    show(n-1)

show(6)

#program to find factorial of a number using recursion

def fact(a):
    
    if(a==0 or a==1):
        return 1
    else:
        return a*fact(a-1)
    

print(fact(5))
