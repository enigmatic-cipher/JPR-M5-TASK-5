"""
Given a number n as input, check whether it is a power of 2.
Input-> 256
Output-> Yes
"""

def power_of_two(n):
  if (n==0):
    return False
  while (n != 1):
    if (n%2 != 0):
      return False
    n = n // 2
  return True

num = int(input("Enter number: "))

if power_of_two(num):
    print("Yes")
else:
    print("No")