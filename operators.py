#arithmetice operators (+,-,*,/,%,**)

a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)    #remainder
print(a ** b)   #a^b

#relational operators (==,!=,>,<,>=,<=)

a = 50
b = 20 

print(a == b)   #bool 
print(a != b)
print(a >= b)
print(a > b)
print(a <= b)
print(a < b)

#assingment operators (=,+=,*=,/=,%=,**=)

num = 10
num = num + 10 #10+10 => 20
# num += 10
# num -= 10
# num *= 10
# num /= 10
# num %= 10
# num **= 10
print("num : ", num)

#logical operators (not,and,or)

    #not
a = 30
b = 30 

print(not False)
print(not True)
print(not(a > b))

    #and
val1 = True
val2 = True

val3 = True
val4 = False

print("ans operator : ", val1 and val2)
print("ans operator : ", val3 and val4)

    #or
val1 = True
val2 = True

val3 = True
val4 = False

a = 40
b = 20

print("or operator : ", val1 or val2)
print("or operator : ", val3 or val4)
print("or operator : ", (a == b) or (a > b))