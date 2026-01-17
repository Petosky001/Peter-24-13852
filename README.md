# AttendanceManagementSystem

NAME = Oshine Onabuchi Peter
MATRIC NO = 24/14176
DEPARTMENT = Cyber Security
COURSE = SEN 201

## 📌 Project Description
AttendanceManagementSystem is a simple Python console-based application that allows teachers to mark student attendance, view attendance records, and save attendance data to a file for future use.

---

## 🚀 Features
- Add student names
- Mark students as Present or Absent
- View attendance records
- Save attendance to file (`attendance.txt`)
- Menu-driven console interface

---

## Project Structure
AttendanceManagementSystem/
│
├── main.py
├── attendance_manager.py
├── file_handler.py
└── README.md


## 🧠 SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC)
1️⃣ Requirement Analysis
Functional Requirements
User can:
Add student names
Mark students as Present or Absent
View attendance records

System should:
Save attendance to a file
Load previous records on startup

Non-Functional Requirements
Python 3
Console-based
Simple and user-friendly

2️⃣ System Design
Architecture
Modular Python program

Component Responsibilities

| File                    | Responsibility   |
| ----------------------- | ---------------- |
| `main.py`               | User interface   |
| `attendance_manager.py` | Attendance logic |
| `file_handler.py`       | File storage     |


3️⃣ Testing
| Scenario            | Expected Result |
| ------------------- | --------------- |
| Add students        | Students stored |
| Mark present/absent | Status updated  |
| Save attendance     | File created    |
| Restart app         | Records persist |

4️⃣ Deployment = GitHub
LINK = https://github.com/Petosky001/Peter-24-13852

5️⃣ Maintenance
Future improvements:
Add date-wise attendance
Export to Excel/CSV
Add student IDs

Build GUI/web version
