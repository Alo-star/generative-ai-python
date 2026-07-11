#take 5 integer in the list and check even number
list1 = {2,4,8,10,20}
for x in list1:
    if(x % 2 == 0):
        print(x)
        
 #take 5 students marks and name,if marks is greater than 50 than give name of students.       
        # Program to display names of students who scored more than 50

students = []
for i in range(5):
    name = input("Enter student name: ")
    marks = int (input("Enter marks: "))
    
    students.append((name, marks)) 

print("\nStudents who scored more than 50:")
for name, marks in students:
    if marks > 50:
        print(name)

#sum of digit  and output is 10
sum =0
for i in range(5):
    number = int (input("Enter number:"))
    sum+=number
    print(sum)

#Reverse a number
rev = 0
num = int (input("Enter number:"))
    
while (num > 0):
    d = num % 10
    rev = (rev * 10) + d
    num //= 10
print(rev)

