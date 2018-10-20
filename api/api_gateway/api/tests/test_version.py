from django.test import TestCase

# Create your tests here.
class VersionTest(TestCase):
    def test_truthiness(self):
        self.assertEqual(True, True)