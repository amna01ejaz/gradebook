class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
        self.marks = {}

    def set_mark(self, subject, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        self.marks[subject] = score

    def average(self):
        if not self.marks:
            return 0.0
        return sum(self.marks.values()) / len(self.marks)

    def to_dict(self):
        return {
            "sid": self.sid,
            "name": self.name,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data):
        s = cls(data["sid"], data["name"])
        s.marks = data.get("marks", {})
        return s


class Gradebook:
    def __init__(self):
        self.students = {}

    def add_student(self, sid, name):
        if sid in self.students:
            raise ValueError("Student already exists")
        self.students[sid] = Student(sid, name)

    def record_mark(self, sid, subject, score):
        if sid not in self.students:
            raise ValueError("Student not found")
        self.students[sid].set_mark(subject, score)

    def subject_topper(self, subject):
        top_sid = None
        top_score = -1

        for sid, student in self.students.items():
            if subject in student.marks:
                if student.marks[subject] > top_score:
                    top_sid = sid
                    top_score = student.marks[subject]

        return top_sid, top_score

    def to_dict(self):
        return {
            "students": [s.to_dict() for s in self.students.values()]
        }

    @classmethod
    def from_dict(cls, data):
        gb = cls()
        for sd in data.get("students", []):
            s = Student.from_dict(sd)
            gb.students[s.sid] = s
        return gb