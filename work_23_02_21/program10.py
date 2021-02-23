"""Declare a function named capitalize_list_items. It takes a list
as a parameter and it returns a
capitalized list of items"""

l=['ram','sita','gita','sakshi','pratik']
def capitalize_list_items(l):
    for i in l:
        r=i.capitalize()
        print(r,end=" ")
capitalize_list_items(l)
