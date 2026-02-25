#WAP to find the sum of first n natural numbers

def cal_sum(a):
    if(a==0):
        return 0
    return cal_sum(a-1) + a
    
sum = cal_sum(5)
print(sum)
    