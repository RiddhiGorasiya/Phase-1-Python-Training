def clac_sum(a,b):
    sum = a + b
    print(sum)
    return sum

clac_sum(5,10)

# more lines of code  

clac_sum(54,8)

# more lines of code

clac_sum(2,5)

# another way to use finctions 

# function definition
def clac_sum(a,b): #parameter
    return a + b

sum = clac_sum(2,3) #funtion call; (1,2) are arguments
print(sum)

def print_hello():
    print("hello")

output = print_hello()
print(output) #None

# average of 3 number 
def clac_avg(a,b,c):
    sum = a + b + c 
    avg = sum / 3
    print(avg)
    return avg

clac_avg(5,5,5)

# buit-in function

print("riddhi", end="$") #sep = " "
print("gorasiya") #end = "\n"

# defult function

def cal_prod(a=1,b=2):
    print(a * b)
    return a * b
 
cal_prod()

#  practice questions
# WAP to print the lenth of a list.(list is the parameter)
cities = ["surat","delhi","gurgaon","noida","pune","mumbai","chennai"]
heroes = ["thor","ironman","captain america","balvir"]
def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

# WAP to print the element of a list in a single line.(list is the parameter)
cities = ["surat","delhi","gurgaon","noida","pune","mumbai","chennai"]
heroes = ["thor","ironman","captain america","balvir"]
def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)

# WAP to find the factorial of n.(n is the parameter)
n = 5
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(5)

# WAP to conver USD to INR.
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(10)