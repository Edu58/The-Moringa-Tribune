from django.test import TestCase
from .models import Editor, Article, Tags


# Create your tests here.
class EditorTestClass(TestCase):
    def setUp(self) -> None:
        self.john = Editor(first_name='john', last_name='doe', email='johndoe@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.john, Editor))

    def test_save_method(self):
        self.john.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
