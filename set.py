collection = {1,2,2,2,"hello","world","world"}
print(collection)
print(type(collection))
print(len(collection)) #total numbers of items

collection = set() #empty dictionary
print(type(collection))

# set method

# add
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("riddhi gorasiya")
collection.add((1,2,3))
print(collection)

# remove
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.remove(1)
print(collection)

# clear
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.remove(1)
collection.clear()
print(len(collection))
print(collection)

# pop 
collection = {"hello","riddhi","world","coding","python"}
print(collection.pop())

# union
set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2))
 
# intersection
set1 = {1,2,3}
set2 = {2,3,4}
print(set1.intersection(set2))

#  practice questions
# you are given a list of subject for student. assume one classroom is required for 1 subject. how many classroom are needed by all student.
    # "python","java","c++","python","javascript"
    # "java","python","java","C++","C"
sub = {
    "python","java","c++","python","javascript","java","python","java","C++","C"
}
print(sub)
print(len(sub))

# figure out a way to store 9 & 9.0 as separate values in the set.(use built-in data type)
values = {9,9.0} # this values are same for the python

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)