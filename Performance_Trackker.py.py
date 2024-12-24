numberOfItems=int(input("Enter the number of students : "))
student={}
for i in range(0,numberOfItems):
    key=input("Enter the key :")
    value=list(map(int,input("Enter the student marks separated with comma :").split(",")))
    student[key]=value
print(student)
avarage_marks={}
for key, marks in student.items():
    total_marks = sum(marks)
    avarage = total_marks / len(marks)  
    avarage_marks[key] = avarage

print("\nAverage Marks:", avarage_marks)
max_student = max(avarage_marks, key=avarage_marks.get)
print("Top performer: ",max_student)