def add(a, b):

    # returning sum of a and b
    return a + b

def is_true(a):

    # returning boolean of a
    return bool(a)

# calling function
res = add(2, 3)
print(res)

res = is_true(2<5)
print(res)

# Returning Multiple Values

def fun():
    name = "Alice"
    age = 30
    return name, age

name, age = fun()
print(name)  
print(age)   # Output: 30

# Returning List

def fun(n):
    return [n**2, n**3]

res = fun(3)
print(res)

# Function returning another function

def fun1(msg):
    def fun2():
        # Using the outer function's message
        return f"Message: {msg}"
    return fun2

# Getting the inner function
fun3 = fun1("Hello, World!")

# Calling the inner function
print(fun3())