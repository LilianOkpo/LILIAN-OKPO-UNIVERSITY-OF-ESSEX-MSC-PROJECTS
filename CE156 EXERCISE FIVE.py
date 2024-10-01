#DEFINE A NAME IN THE LOCAL NAME-SPACE FOR THE SCOPE WHERE THE IMPORT STATEMENT OCCURS
import numpy as np

#ASK THE USER FOR THE FILE NAME
file_name = input("Enter the file name: ")

with open(file_name, 'r') as file:
    #READ THE FIRST LINE TO GET THE NUMBER OF STUDENTS AND THE COURSE WORK WEIGHT
    first_line = file.readline().split()
    num_of_students = int(first_line[0])
    coursework_weight = float(first_line[1])

    #CREATE A 2-DIMENSIONAL NUMPY ARRAY
    students_marks_array = np.array([[0, 0.0, 0.0, 0.0]] * num_of_students, dtype=float)

    #READ AND PROCESS THE REMAINING LINES, LINE BY LINE
    for i, line in enumerate(file):
        data = line.split()
        if len(data) >= 3:       # #TO MAKE SURE THERE ARE AT LEAST 3 ELEMENTS IN THE LINE
            try:
                Reg_number = int(data[0])
                Exam_mark = float(data[1])
                Coursework_mark = float(data[2])

                #TO CHECK IF ANY MARK IS BELOW 30
                if Exam_mark < 30 or Coursework_mark < 30:
                    Module_overall_mark = min(Exam_mark, Coursework_mark)
                else:
                    Module_overall_mark = (Exam_mark * (100 - coursework_weight) + Coursework_mark * coursework_weight) / 100

                #STORE THE VALUES IN THE NUMPY ARRAY
                students_marks_array[i] = [Reg_number, Exam_mark, Coursework_mark, Module_overall_mark]
            except (ValueError, IndexError):
                print(f"Issue processing line {i+2}.Skip")  # #ADDING 2 TO 'i' ACCOUNT FOR THE 0-BASED INDEX AND THE HEADER LINE
        else:
            print(f"Invalid data format in line {i+2}.Skip")

#DEFINE A FUNCTION FOR THE NAMED DATA TYPE
studType = np.dtype([('Reg_number', int), ('Exam_mark', int), ('Coursework_mark', int), ('Module_overall_mark', int), ('grade', 'U15')])

#CREATE A 1-DIMENSIONAL ARRAY USING THE NAMED studType AS A DTYPE ARGUMENT IN THE CALL TO np.array
student_data = np.array([(0, 0, 0, 0, '')] * len(students_marks_array), dtype=studType)

#CALCULATE AND ASSIGN VALUES TO THE STRUCTURED ARRAY
for i in range(len(students_marks_array)):
    Reg_number, Exam_mark, Coursework_mark, Module_overall_mark = students_marks_array[i]

    #DEFINE THE FUNCTION RULES FOR CALCULATING THE GRADES
    if Module_overall_mark < 30:
        grade = 'F'
    elif Module_overall_mark >= 70:
        grade = 'FIRST CLASS'
    elif 50 <= Module_overall_mark <= 69:
        grade = 'SECOND CLASS'
    elif 40 <= Module_overall_mark <= 49:
        grade = 'THIRD CLASS'
    else:
        grade = 'F'

    #ASSIGN VALUES TO THE STRUCTURED ARRAY
    student_data[i] = (Reg_number, int(Exam_mark), int(Coursework_mark), round(Module_overall_mark), grade)

#SORT THE SECOND ARRAY BY THE MODULE_OVERALL_MARK
array2 = np.sort(student_data, order='Module_overall_mark')[::-1]  # #SORT IN DESCENDING ORDER

#WRITE THE SORTED ARRAY TO A FILE
with open('array2', 'w') as f:
    print(array2, file=f)

#CALCULATE THE NUMBER OF STUDENTS IN EACH GRADE CATEGORY AND COUNT THE STUDENTS THAT FAILED
grade_counts = {'FIRST CLASS': 0, 'SECOND CLASS': 0, 'THIRD CLASS': 0, 'F': 0}
The_Failed_Students = []

for student in student_data:
    grade = student['grade']
    if grade == 'F':
        The_Failed_Students.append(student['Reg_number'])
    grade_counts[grade] += 1

#OUTPUT THE NUMBER OF STUDENTS IN EACH GRADE CATEGORY
print("Number Of Students In Each Grade Category:")
for grade, count in grade_counts.items():
    print(f"{grade}: {count}")

#OUTPUT THE NUMBER OF STUDENTS THAT FAILED AND THEIR REGISTRATION NUMBERS
num_failed_students = grade_counts['F']
print(f"Number Of Failed Students: {num_failed_students}")
print("Registration Numbers of Failed Students:")
print(The_Failed_Students)
