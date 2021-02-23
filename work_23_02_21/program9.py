""" Declare a function named reverse_list. It takes an array as a parameter
and it returns the reverse of the array (use loops).

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"] """

l=[5,4,3,2,1]
v=["A", "B", "C"]

def reverse_list(lis):
    e = []
    for item in lis:
        e.insert(0,item)
    return e
r = reverse_list(l)
r1 = reverse_list(v)
print('Reverse List is : ',r)
print('Reverse List is : ',r1)
