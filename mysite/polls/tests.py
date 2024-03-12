from django.test import TestCase
from .models import YourModel

class YourModelTestCase(TestCase):
    def setUp(self):
        # Create test data for the model
        YourModel.objects.create(name='John', age=30, email='john@example.com')

    def test_model_creation(self):
        # Retrieve the test data and perform assertions
        john = YourModel.objects.get(name='John')
        self.assertEqual(john.age, 30)
        self.assertEqual(john.email, 'john@example.com')
