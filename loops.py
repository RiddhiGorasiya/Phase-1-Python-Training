# # while loop

count = 1
while count <= 5 :
    print("Hello")
    count += 1 

i = 1
while i <= 5:
    print("Riddhi Gorasiya", i)
    i += 1

# practice questions
# # print number from 1 to 100.
i = 1 
while i <= 100:
    print(i)
    i += 1

# # print number from 100 to 1.
i = 100
while i >= 1: #stopping condition
    print(i)
    i -= 1

# # print the multiplication table of a number
n = int(input("Enter number : "))
i = 1
while i <= 10:
    print(n*i)
    i += 1 

# # print the elements of the follwing list using a loop:
# # [1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]
inx = 0
while inx < len(nums):
    print(nums [inx]) #nums[0], nums[1], nums[2] .....
    inx += 1
     
# # search for a number x in this tuple using loop:
# [1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]
x = 36
i = 0 #initialization
while i < len(nums):
    if(nums[i] == x):
        print("Found at idx ", i)
    i += 1 


# *********************************

# break key word for while loop
i = 1 
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1

print("End of loop")

nums = [1,4,9,16,25,36,49,64,81,100]
x = 36
i = 0 #initialization
while i < len(nums):
    if(nums[i] == x):
        print("Found at idx ", i)
        break
    else:
        print("Finding..")
    i += 1 
print("End of loop")

# # continue key word for while loop 
i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue 
    print(i)
    i += 1

i = 0 #odd
while i <= 5:
    if(i%2 == 0):
        i += 1
        continue 
    print(i)
    i += 1

i = 0 #even
while i <= 5:
    if(i%2 != 0):
        i += 1
        continue 
     

# **************************

# for loop 

nums = [1,2,3,4,5]
for val in nums:
    print(val)

vaggies = ["potato","brijal","ladyfinger","cucumber"]
for val in vaggies:
    print(val)

# for loop with else
str = "riddhigorasiya"
for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)
else:
    print("END")

# practice questions
# # print thr elements of the follwoing list using a loop:
# [1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]
for el in nums :
    print(el)

# # search for a number x in this tuple using loop:
# # [1,4,9,16,25,36,49,64,81,100]
nums = (1,4,9,16,25,36,49,64,81,100,49)
x = 49
idx = 0 
for el in nums :
    if(el == x):
        print("Number found at inx :",idx) 
    idx += 1

# ******************************

# range for the for loop

for i in range(10): #range(stop)
    print(i)

for i in range(2,10): #range(start,stop)
    print(i)

for i in range(2,10,2): #range(start,stop,sep) #print even number
    print(i)

for i in range(1,10,2): #range(start,stop,sep) #print odd number
    print(i)

# pass statement in loop 

for i in range(5):
    pass
if i > 5:
    pass
print("Some useful work")

# ****************************

# practice questions
# WAP to find the sum of first n number.(using while)
n = 7
sum = 0
i = 1 
while i <= n:
    sum += i
    i += 1
print("Total sum =", sum)

# WAP to find the factorial of first n number.(using for)
n = 7
fact = 1
i = 1 
while i <= n:
    fact *= i
    i += 1
print("Total factorial =", fact)