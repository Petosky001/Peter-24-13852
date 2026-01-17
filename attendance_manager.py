def create_student(name):
    return {
        "name": name,
        "status": "Absent"
    }


def mark_present(student):
    student["status"] = "Present"


def mark_absent(student):
    student["status"] = "Absent"
