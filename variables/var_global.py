x = "awesome"

def my_func():
    print("Python is " + x) 

my_func()

# In this example, the variable x was defined in the global scope
# When this happen, it's possible to access this variable inside functions


def my_func_two():
    x = "fantastic"
    print("Pythob is " + x)

my_func_two()
print("Python is " + x)

# When we create a variable inside a function, this mean that, the this variable scope is visible only inside a function.

# global keyword means that inside a function, it's possible to change a value of global variable.

def my_func_tree():
    global x
    x = "fantastic"
    print("Python is " + x)

my_func_tree()

print("Python is " + x)