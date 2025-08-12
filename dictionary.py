info ={
 "name" : "riddhi",
 "subject" : ["python","C","java"],
 "topices" : ("dict","set"),
 "age" : 34,
 "is_adult" : True,
 "marks" : 7.83
}
print(info)
print(info["name"])
print(type(info))

nul_dict = {}

# nested dictionaries

student = {
    "name" : "heni",
    "subject" : {
        "phy" : 87,
        "chem" : 65,
        "math" : 65
    }
}
print(student)
print(student["subject"])
print(student["subject"]["math"])

# dictionary methods

# key
student = {
    "name" : "heni",
    "subject" : {
        "phy" : 87,
        "chem" : 65,
        "math" : 65
    }
}
print(student.keys())

# values
student = {
    "name" : "heni",
    "subject" : {
        "phy" : 87,
        "chem" : 65,
        "math" : 65
    }
}
print(student.values())
print(list(student.values()))


# items
student = {
    "name" : "heni",
    "subject" : {
        "phy" : 87,
        "chem" : 65,
        "math" : 65
    }
}
print(student.items())
print(list(student.items()))

# get
student = {
    "name" : "heni",
    "subject" : {
        "phy" : 87,
        "chem" : 65,
        "math" : 65
    }
}
print(student.get("subject"))
print(student["name"])

# update
student = {
    "name" : "heni",
    "subject" : {
        "phy" : 87,
        "chem" : 65,
        "math" : 65
    }
}
new_dict = {"city" : "surat" , "age" : 20}
student.update(new_dict)
print(student)

#  practice questions
# Store following word meanings in a python dictionary: 
    # table : "a piece of furniture", "list of facts & figures"
    # cat : "a small animal"
dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]
}
print(dictionary)

# WAP to enter marks of 3 subject from the user and store them in a dictionary, start with an empty dictionary & add by one. use subject as key & marks as value.
marks = {}
x = int(input("Enter phy : "))
marks.update({"phy" : x})

x = int(input("Enter math : "))
marks.update({"math" : x})

x = int(input("Enter chem : "))
marks.update({"chem" : x})

print(marks)
