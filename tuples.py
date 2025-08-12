tup = (1,2,3,4)
print(tup[0])

tup = () #its empty tuple
print(tup)
print(type(tup))

# tuple method

tup = (1,2,3,4)
print(tup.index(2)) #(2) is element

# tuple count

tup = (1,2,3,4,2,5,2,2)
print(tup.count(2))

#  practice questions
# WAP to count the number of students with "A" grade in the following tuple.
grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))

# store the above values in a list & sort them "A" to "D".
grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)