from models import Gradebook


class GradebookApp:
    def __init__(self, storage):
        self.storage = storage
        self.gradebook = Gradebook()

    def load(self):
        data = self.storage.load()
        self.gradebook = Gradebook.from_dict(data)

    def save(self):
        data = self.gradebook.to_dict()
        self.storage.save(data)
    def delete_student(self, sid):
     if sid not in self.students:
        raise ValueError("Student not found")
     del self.students[sid]