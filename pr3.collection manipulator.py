
students = []
subjects_set = set()
student_data = {}

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Student ID: ")
        name = input("Name: ").title()
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth: ")
        subjects = input("Subjects: ")

        subjects = [s.strip().title() for s in subjects]

        student = {
            "ID": sid, "Name": name, "Age": age,
            "Grade": grade, "DOB": dob,
            "Info": (sid, dob), "Subjects": subjects
        }

        students.append(student)
        student_data[sid] = student
        subjects_set.update(subjects)
        print("Student added!")

    elif choice == "2":
        for s in students:
            print(f"{s['ID']} | {s['Name']} | {s['Age']} | {s['Grade']} | {s['Subjects']}")

    elif choice == "3":
        sid = input("Student ID: ")
        if sid in student_data:
            student_data[sid]["Age"] = int(input("New age: "))
            print("Student updated!")
        else:
            print("Student not found.")

    elif choice == "4":
        sid = input("Student ID: ")
        if sid in student_data:
            for i in range(len(students)):
                if students[i]["ID"] == sid:
                    del students[i]
                    break
            del student_data[sid]
            print("Student deleted!")
        else:
            print("Student not found.")

    elif choice == "5":
        subjects_set = set()
        for s in students:
            subjects_set.update(s["Subjects"])
        print(subjects_set)

    elif choice == "6":
        print("Exit")
        break

    else:
        print("Invalid choice.")