""" Declare a function named sum_of_numbers.
It takes a number parameter and it adds all the numbers in that range.
print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050 """

def sum_of_numbers(a):
    i=0
    sum=0
    while i<a+1:
        sum=sum+i
        i+=1
    return sum
s=sum_of_numbers(int(input("enter number you want to add")))
print(f"the some of number is {s}")
