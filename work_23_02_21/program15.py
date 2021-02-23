"""Use for loop to iterate from 0 to 100
and print the sum of all evens and the sum of all odds.

The sum of all evens is 2550. And the sum of all odds is 2500."""
s=0
n=0
for i in range(0,101):
    if i%2==0:
        s=s+i
    if i%2==1:
        n=n+i
print(f"sum of even numbers of given range is = ",s)
print(f"sum of odd numbers of given range is = ",n)
