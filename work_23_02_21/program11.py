""" Declare a function named add_item.
It takes a list and an item parameters.
It returns a list with the item added at the end.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(  add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]"""

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
def add_item(l,a):
        food_staff.append(a)
        
add_item(food_staff,input("enter any element"))
print(food_staff)
