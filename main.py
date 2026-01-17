from attendance_manager import create_student, mark_present, mark_absent
from file_handler import save_attendance, load_attendance


def main():
    print("=== Attendance Management System ===")
    students = load_attendance()

    if not students:
        print("No students found. Please add students.")
        while True:
            name = input("Enter student name (or type 'done' to finish): ")
            if name.lower() == "done":
                break
            students.append(create_student(name))

    while True:
        print("\n1. Mark Present")
        print("2. Mark Absent")
        print("3. View Attendance")
        print("4. Save Attendance")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter student name: ")
            for student in students:
                if student["name"].lower() == name.lower():
                    mark_present(student)
                    print(f"{name} marked Present.")
                    break
            else:
                print("Student not found.")

        elif choice == "2":
            name = input("Enter student name: ")
            for student in students:
                if student["name"].lower() == name.lower():
                    mark_absent(student)
                    print(f"{name} marked Absent.")
                    break
            else:
                print("Student not found.")

        elif choice == "3":
            print("\n--- Attendance Records ---")
            for student in students:
                print(f"{student['name']} - {student['status']}")

        elif choice == "4":
            save_attendance(students)
            print("Attendance saved successfully.")

        elif choice == "5":
            save_attendance(students)
            print("Exiting Attendance Management System...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
