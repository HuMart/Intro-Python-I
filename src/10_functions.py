# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def is_even(n):
    if n % 2 == 0:
        return True
    elif n % 2 == 1:
        return False

if is_even(num):
    print("Even")
elif not is_even(num):
    print("Odd")