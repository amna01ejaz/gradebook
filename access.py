from models import Student, Gradebook


class AccessController:
    """Handles validation and safe access to Gradebook"""

    def __init__(self, gradebook: Gradebook, role="user"):
        self.gradebook = gradebook
        self.role = role   # "admin" or "user"

    # -----------------------------
    # ROLE CHECK
    # -----------------------------
    def _is_admin(self):
        return self.role == "admin"

    # -----------------------------
    # STUDENT METHODS
    # -----------------------------
    def add_student(self, student_id, name):
        if not self._is_admin():
            raise PermissionError("Only admin can add students")

        if not student_id or not name:
            raise ValueError("Student ID and name cannot be empty")

        student = Student(student_id, name)
        self.gradebook.add_student(student)

    def remove_student(self, student_id):
        if not self._is_admin():
            raise PermissionError("Only admin can remove students")

        if student_id not in self.gradebook.students:
            raise ValueError("Student not found")

        del self.gradebook.students[student_id]

    # -----------------------------
    # MARKS METHODS
    # -----------------------------
    def add_mark(self, student_id, subject, marks):
        if not self._is_admin():
            raise PermissionError("Only admin can add marks")

        if student_id not in self.gradebook.students:
            raise ValueError("Student not found")

        if not subject:
            raise ValueError("Subject cannot be empty")

        if not (0 <= marks <= 100):
            raise ValueError("Marks must be between 0 and 100")

        student = self.gradebook.students[student_id]
        student.add_mark(subject, marks)

    # -----------------------------
    # VIEW METHODS
    # -----------------------------
    def view_student(self, student_id):
        if student_id not in self.gradebook.students:
            raise ValueError("Student not found")

        student = self.gradebook.students[student_id]

        return {
            "id": student.student_id,
            "name": student.name,
            "marks": student.marks,
            "average": student.average()
        }

    def list_students(self):
        return [
            {
                "id": s.student_id,
                "name": s.name,
                "average": s.average()
            }
            for s in self.gradebook.students.values()
        ]