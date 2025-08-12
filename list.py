marks = [54.5,65.4,98.5,54.8,98.7]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[3])

student = ["riddhi",87.54,20,"surat"]
print(student[0])
student[0] = "heni"
print(student)

# list slicing

marks = [54,65,98,54,98]
print(marks[2:4])
print(marks[:2])
print(marks[2:])
print(marks[-3:-1])

# list method

# append
list = [2,1,3]
list.append(5)
print(list)

# sort
list = [2,1,3]
print(list.sort())
print(list)

# descending 
list = [2,1,3]
print(list.sort(reverse=True))
print(list)

list1 = ["banana","litchi","apple"]
print(list1.sort(reverse=True))
print(list1)

#  practice questions
# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
movies = []
movies.append(input("Enter 1st movie: "))
movies.append(input("Enter 2nd movie: "))
movies.append(input("Enter 3rd movie: "))
print(movies)

# WAP to check if a list contains a palindrome of element.
# [1,2,3,2,1] [1,"abc","abc",1] its call palindrome
list1 = [1,2,1]
list2 = [1,2,3]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Pelindrom")