from django.test import TestCase
from todos.models import Task
from account.models import ToDoUser
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber

class TaskTestCase(TestCase):
    def setUp(self):

        self.user = ToDoUser.objects.create(email="test@gmail.com",first_name ="Test",phone_number=PhoneNumber.from_string("+917007975402"))
        self.task_one = Task.objects.create(title="My Test Task One", owner=self.user,active=False)
        self.task_two = Task.objects.create(title="My Test Task One", owner=self.user)

    def test_search(self):
        """Animals that can speak are correctly identified"""
        task = Task.objects.get_queryset().search("My")
        self.assertEqual(task.count(),2)

    def test_active(self):
        task = Task.objects.all()
        self.assertEqual(task.count(),1)

    def test_all_in_active(self):
        task = Task.objects.all_inactive()
        self.assertEqual(task.count(),1)


