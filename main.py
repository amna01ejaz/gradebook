from storage import JsonFileStorage
from app import GradebookApp


def menu():
    print("\n--- Gradebook ---")
    print("1. Add Student")
    print("2. Add Mark")
    print("3. Show Average")
    print("4. Subject Topper")
    print("5. Save")
    print("6. Load")
    print("7. Exit")
    print("8. Delete Student")


def main():
    storage = JsonFileStorage("data.json")
    app = GradebookApp(storage)
    app.load()

    while True:
     menu()
     choice = input("Choose: ")

     try:
        if choice == "1":
            sid = input("Student ID: ")
            name = input("Name: ")
            app.gradebook.add_student(sid, name)
            print("Student added")

        elif choice == "2":
            sid = input("Student ID: ")
            subject = input("Subject: ")
            score = float(input("Score: "))
            app.gradebook.record_mark(sid, subject, score)
            print("Mark added")

        elif choice == "3":
            sid = input("Student ID: ")
            student = app.gradebook.students[sid]
            print("Average:", student.average())

        elif choice == "4":
            subject = input("Subject: ")
            sid, score = app.gradebook.subject_topper(subject)
            print("Topper:", sid, "Score:", score)

        elif choice == "5":
            app.save()
            print("Saved")

        elif choice == "6":
            app.load()
            print("Loaded")

        elif choice == "7":
            app.save()
            print("Goodbye")
            break

        elif choice == "8":   
            sid = input("Student ID: ")
            app.gradebook.delete_student(sid)
            print("Student deleted")

        else:
            print("Invalid choice")

     except Exception as e:
        print("Error:", e)
        if __name__ == "__main__":
         main()