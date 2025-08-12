#if statement
    #If statement is the simplest form of a conditional statement. It executes a block of code if the given condition is true.

age = 20
if (age > 18):
    print("cam Vote & apply for license.")

#if else statement
    #Else allows us to specify a block of code that will execute if the condition(s) associated with an if or elif statement evaluates to False. Else block provides a way to handle all other cases that don't meet the specified conditions.
    
age = 10

if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")

marks = 45
res = "Pass" if marks >= 40 else "Fail"

print(f"Result: {res}")

#elif statement
    #elif statement in Python stands for "else if." It allows us to check multiple conditions , providing a way to execute different blocks of code based on which condition is true. Using elif statements makes our code more readable and efficient by eliminating the need for multiple nested if statements.
    
age = 50

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")