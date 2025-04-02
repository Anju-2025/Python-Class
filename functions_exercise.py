# # # STUDENT MANAGEMENT SYSTEM

# # # Function to add a new student
# def add_student():
#     students=[]
#     name = input("Enter student's name: ")
#     grades = input("Enter student's grades separated by commas: ").split(",")
#     grades = [int(grade) for grade in grades]  # Convert grades to integers
#     students.append({"name": name, "grades": grades})
#     print(f"Student {name} has been added successfully!")

# # Function to view all students
# def view_students(students):
#     if not students:
#         print("No students available.")
#         return
#     print("\nList of all students:")
#     for student in students:
#         print(f"Name: {student['name']}, Grades: {student['grades']}")

# # Function to search for a student by name
# def search_student(students):
#     name = input("Enter the student's name to search: ")
#     found = False
#     for student in students:
#         if student['name'].lower() == name.lower():
#             print(f"Found student: {student['name']}, Grades: {student['grades']}")
#             found = True
#             break
#     if not found:
#         print(f"Student {name} not found.")

# # Function to remove a student by name
# def remove_student(students):
#     name = input("Enter the student's name to remove: ")
#     for student in students:
#         if student['name'].lower() == name.lower():
#             students.remove(student)
#             print(f"Student {name} has been removed successfully.")
#             return
#     print(f"Student {name} not found.")

# # Function to calculate the average grade of all students
# def calculate_average_grade(students):
#     if not students:
#         print("No students available to calculate the average.")
#         return
#     total_grades = 0
#     total_students = 0
#     for student in students:
#         total_grades += sum(student['grades'])
#         total_students += len(student['grades'])
#     average = total_grades / total_students
#     print(f"The average grade of all students is: {average:.2f}")

# # Main program loop
# def student_management_system():
#     students = []  # List to store students
#     while True:
#         print("\nChoose an option:")
#         print("1. Add Student")
#         print("2. View All Students")
#         print("3. Search for Student")
#         print("4. Remove Student")
#         print("5. Calculate Average Grade")
#         print("6. Exit")

#         choice = input("Enter your choice (1-6): ")

#         if choice == '1':
#             add_student()
#         elif choice == '2':
#             view_students()
#         elif choice == '3':
#             search_student()
#         elif choice == '4':
#             remove_student()
#         elif choice == '5':
#             calculate_average_grade()
#         elif choice == '6':
#             print("Exiting the system. Goodbye!")
#             break
#         else:
#             print("Invalid option. Please try again.")

# # # Run the student management system
# student_management_system()



# # Function to add a new student
# def add_student(students):
#     name = input("Enter student's name: ")
#     grades = input("Enter student's grades separated by commas: ").split(",")
#     grades = [int(grade) for grade in grades]  # Convert grades to integers
#     students.append({"name": name, "grades": grades})
#     print(f"Student {name} added.")

# # Function to view all students
# def view_students(students):
#     if not students:
#         print("No students available.")
#         return
#     print("\nList of all students:")
#     for student in students:
#         print(f"Name: {student['name']}, Grades: {student['grades']}")

# # Function to search for a student by name
# def search_student(students):
#     name = input("Enter the student's name to search: ")
#     for student in students:
#         if student['name'].lower() == name.lower():
#             print(f"Found student: {student['name']}, Grades: {student['grades']}")
#             return
#     print(f"Student {name} not found.")

# # Main program loop
# def student_management_system():
#     students = []  # List to store students
#     while True:
#         print("\nChoose an option:")
#         print("1. Add Student")
#         print("2. View All Students")
#         print("3. Search for Student")
#         print("4. Exit")

#         choice = input("Enter your choice (1-4): ")

#         if choice == '1':
#             add_student(students)
#         elif choice == '2':
#             view_students(students)
#         elif choice == '3':
#             search_student(students)
#         elif choice == '4':
#             print("Exiting the system. Goodbye!")
#             break
#         else:
#             print("Invalid option. Please try again.")

# # Run the student management system
# student_management_system()




# Function to add a new student with grades restricted to 5 marks per exam (max 50)
# def add_student(students):
#     name = input("Enter student's name: ")
#     grades = []
    
#     # Adding only 5 marks per exam, and ensuring it's within the allowed range (max 50)
#     for i in range(5):  # Assume 5 subjects (or exams)
#         while True:
#             try:
#                 grade = int(input(f"Enter grade for subject {i+1} (0 to 50): "))
#                 if 0 <= grade <= 50:
#                     grades.append(grade)
#                     break
#                 else:
#                     print("Grade must be between 0 and 50. Please try again.")
#             except ValueError:
#                 print("Invalid input. Please enter a number between 0 and 50.")
    
#     students.append({"name": name, "grades": grades})
#     print(f"Student {name} added.")

# # Function to view all students
# def view_students(students):
#     if not students:
#         print("No students available.")
#         return
#     print("\nList of all students:")
#     for student in students:
#         print(f"Name: {student['name']}, Grades: {student['grades']}")

# # Function to search for a student by name
# def search_student(students):
#     name = input("Enter the student's name to search: ")
#     for student in students:
#         if student['name'].lower() == name.lower():
#             print(f"Found student: {student['name']}, Grades: {student['grades']}")
#             return
#     print(f"Student {name} not found.")

# # Main program loop
# def student_management_system():
#     students = []  # List to store students
#     while True:
#         print("\nChoose an option:")
#         print("1. Add Student")
#         print("2. View All Students")
#         print("3. Search for Student")
#         print("4. Exit")

#         choice = input("Enter your choice (1-4): ")

#         if choice == '1':
#             add_student(students)
#         elif choice == '2':
#             view_students(students)
#         elif choice == '3':
#             search_student(students)
#         elif choice == '4':
#             print("Exiting the system. Goodbye!")
#             break
#         else:
#             print("Invalid option. Please try again.")

# # Run the student management system
# student_management_system()


# Write a program that allows a user to:

# Add a number to the list.
# Remove a number from the list.
# Display the maximum number in the list.
# Display the minimum number in the list.
# Calculate the sum of all numbers in the list.
# Display all numbers in the list.
# Exit the program.
# Each operation should be a separate function, and the program should continue until the user chooses to exit.

# Initialize an empty list
# numbers = []

# #  Define each function
# def add_number(num):
#     numbers.append(num)
#     print(f"{num} added to the list.")

# def remove_number(num):
#     if num in numbers:
#         numbers.remove(num)
#         print(f"{num} removed from the list.")
#     else:
#         print(f"{num} not found in the list.")

# def find_max():
#     if numbers:
#         return max(numbers)
#     else:
#         return "List is empty."

# def find_min():
#     if numbers:
#         return min(numbers)
#     else:
#         return "List is empty."

# def calculate_sum():
#     return sum(numbers)

# def display_numbers():
#     if numbers:
#         print("Current numbers in the list:", numbers)
#     else:
#         print("List is empty.")

# # Main program loop
# while True:
#     print("\nSelect operation:")
#     print("1. Add a number")
#     print("2. Remove a number")
#     print("3. Display the maximum number")
#     print("4. Display the minimum number")
#     print("5. Calculate the sum of all numbers")
#     print("6. Display all numbers")
#     print("7. Exit")

#     choice = input("Enter choice (1/2/3/4/5/6/7): ")

#     if choice == '7':
#         print("Exiting program.")
#         break

#     if choice == '1':
#         num = int(input("Enter a number to add: "))
#         add_number(num)
#     elif choice == '2':
#         num = int(input("Enter a number to remove: "))
#         remove_number(num)
#     elif choice == '3':
#         print("Maximum number in the list:", find_max())
#     elif choice == '4':
#         print("Minimum number in the list:", find_min())
#     elif choice == '5':
#         print("Sum of all numbers:", calculate_sum())
#     elif choice == '6':
#         display_numbers()
#     else:
#         print("Invalid choice! Please try again.")


# # d=[10,20,30]
# # print(sum(d))
# # print(min(d))

