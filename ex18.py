# unpacking args  Notice how he unpacks args nice way of doing it
def print_two(*args):
    arg1,arg2= args
    print(f"args1:{arg1},args:{arg2}")

# This takes two arguments
def print_two_again(arg1,arg2):
    print(f"arg1: {arg1},arg2: {arg2}")

# This takes one argument
def print_one(arg1):
    print(f"arg1:{arg1}")

# This takes no argument
def print_none():
    print("I got nothin'.")


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()