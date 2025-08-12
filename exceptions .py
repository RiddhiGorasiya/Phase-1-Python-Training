# try & except

try:
    # Code that may raise an exception
    x = 3 / 0
    print(x)
except:
    # exception occurs, if code under try throws error
    print("An exception occurred.")

def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")

# Look at parameters and note the working of Program
divide(20,10)

# finally

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught division by zero error.")
finally:
    print("This block always executes.")

try:
    k = 5 // 1
    print(k)
finally:
    print('This is always executed')

# raise

def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)