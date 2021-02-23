"""Declare a function named sum_of_odds.
It takes a number parameter and it adds all the odd numbers in that range."""

def sum_of_odds(a):
    i=0
    s=0
    while i<a+1:
        if i%2==1:
            s=s+i
        i+=1
    return s
print(sum_of_odds(int(input("enter number"))))
    
    
