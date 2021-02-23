""" Declare a function named remove_item.
It takes a list and an item parameters.
It returns a list with the item removed from it.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9] """


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
def remove_item(l,a):
    r=a.capitalize()
    for i in l:
        if r in i:
            food_staff.remove(r)
remove_item(food_staff,input("enter element you want to remove"))
print(food_staff)
