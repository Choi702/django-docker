from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import rvhome

class motorhomeTests(TestCase):

    @classmethod

    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_rvhome = rvhome.objects.create(
            owner = testuser1,
            title = 'Green Eggs and Ham',
            specification = 'I do not like green eggs and ham, Sam I  am.'
        )
        test_rvhome.save()

    def test_rvhome_content(self):
        rv = rvhome.objects.get(id=1)
        actual_owner = str(rv.owner)
        actual_title = str(rv.title)
        actual_specification = str(rv.specification)
        self.assertEqual(actual_owner, 'testuser1')
        self.assertEqual(actual_title, 'Green Eggs and Ham')
        self.assertEqual(actual_specification, 'I do not like green eggs and ham, Sam I  am.')
        
