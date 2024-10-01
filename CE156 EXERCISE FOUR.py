#IMPORT STATEMENT
import csv
#DEFINE THE FUNCTION THAT TAKES TWO ARGUMENTS-A LIST OF TUPLES AND A STRING CONTAINING THE NAME OF A DEPARTMENT
def filter_students_by_department(students, department):
    matching_students = [student for student in students if student[2].lower() == department.lower()]
    return matching_students
#DEFINE THE FUNCTION THAT ASKS THE USER TO SUPPLY A FILE NAME AND ATTEMPTS TO OPEN AND READ THE FILE
def main():
    file_name = input("Enter the name of the CSV file: ")
    try:
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            the_students_list = [tuple(row) for row in reader]  # #THE PROGRAM CONVERTS THE CONTENT OF EACH LINE INTO A TUPLE

        print("List Of Tuples:")
        print(the_students_list)
        #AFTER THE PROGRAM OUTPUTS A LIST OF TUPLES, A LOOP FUNCTION IS ENTERED IN WHICH THE USER IS ASKED TO SUPPLY THE NAME OF A DEPARTMENT
        while True:
            student_department_input = input("Enter The Name Of A Department (Or Type 'quit' To Exit): ")

            if student_department_input.lower() == 'quit':
                break
            else:
                matching_students = filter_students_by_department(the_students_list, student_department_input)  # #STUDENTS ARE FILTERED BY DEPARTMENT

                if matching_students:
                    print("Name\tRegistration Number\tDepartment")
                    for student in matching_students:
                        print(f"{student[0]}\t{student[1]}\t\t\t{student[2]}")
                    break
                else:
                    #AFTER RETURNING FROM THE FUNCTION, THE USER IS ASKED IF HE/SHE WISHES TO SUPPLY THE NAME OF ANOTHER DEPARTMENT OR QUIT
                    print(f"No students found in the {student_department_input} department. Please try again or type 'quit' to exit.")
    except FileNotFoundError:
        print(f"File '{file_name}' Is Not Found!")

if __name__ == "__main__":
    main()
