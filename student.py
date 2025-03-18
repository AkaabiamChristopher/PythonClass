from student import student

def create_student():
    print("Please enter your details:")
    user_id = input("User ID: ")
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    return student(user_id, name, email, password)


if __name__ == "__main__":
    student = create_student()
    print("\nStudent created successfully!")
    print(f"Name: {student.name}")
    print(f"Email: {student.email}")

    while True:
        print("\nOptions:")
        print("1. Enroll in a course")
        print("2. View enrolled courses")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            course = input("Enter the course name to enroll: ")
            student.enroll_in_course(course)
        elif choice == "2":
            print("Enrolled Courses:", student.view_courses())
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")