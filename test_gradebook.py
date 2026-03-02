import unittest
from models import Student, Gradebook
from storage import MemoryStorage
from app import GradebookApp


class TestGradebook(unittest.TestCase):

    def test_average_empty(self):
        s = Student("S1", "Ayesha")
        self.assertEqual(s.average(), 0.0)

    def test_add_student(self):
        gb = Gradebook()
        gb.add_student("S1", "Ayesha")
        self.assertIn("S1", gb.students)

    def test_record_mark(self):
        gb = Gradebook()
        gb.add_student("S1", "Ayesha")
        gb.record_mark("S1", "Math", 90)
        self.assertEqual(gb.students["S1"].marks["Math"], 90)

    def test_invalid_mark(self):
        s = Student("S1", "Ayesha")
        with self.assertRaises(ValueError):
            s.set_mark("Math", 150)

    def test_topper(self):
        gb = Gradebook()
        gb.add_student("S1", "Ayesha")
        gb.add_student("S2", "Hassan")

        gb.record_mark("S1", "Math", 80)
        gb.record_mark("S2", "Math", 95)

        sid, score = gb.subject_topper("Math")
        self.assertEqual(sid, "S2")
        self.assertEqual(score, 95)

    def test_save_load(self):
        storage = MemoryStorage()
        app = GradebookApp(storage)

        app.gradebook.add_student("S1", "Ayesha")
        app.save()

        new_app = GradebookApp(storage)
        new_app.load()

        self.assertIn("S1", new_app.gradebook.students)


if __name__ == "__main__":
    unittest.main()
  