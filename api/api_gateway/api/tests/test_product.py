from django.test import TestCase

# Create your tests here.
class ProductTest(TestCase):
    def test_truthiness(self):
        self.assertEqual(True, True)