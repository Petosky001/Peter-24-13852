def save_attendance(students):
    with open("attendance.txt", "w") as file:
        for student in students:
            file.write(f"{student['name']},{student['status']}\n")


def load_attendance():
    students = []
    try:
        with open("attendance.txt", "r") as file:
            for line in file:
                name, status = line.strip().split(",")
                students.append({
                    "name": name,
                    "status": status
                })
    except FileNotFoundError:
        pass
    return students
