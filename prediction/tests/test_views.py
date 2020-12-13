from django.urls import reverse
from prediction.models import Test,users,admit
import json
from django.test import TestCase,Client
from django.contrib.auth.models import User
class Testview(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('chinni', 'chinni@gmail.com', 'chinni123')
        self.response=self.client.login(username='chinni', password='chinni123')
    def test_signup_get(self):
        client=Client()
        response=client.get(reverse('signup'))
        self.assertTemplateUsed(response,"signup.html")
    def test_login_get(self):
        
        self.response=self.client.get(reverse('login'))
        self.assertTemplateUsed(self.response,"login.html")
        self.assertEqual(self.response.status_code, 200)
    def test_home_get(self):
        self.response=self.client.get(reverse('home'))
        self.assertTemplateUsed(self.response,"home.html")
        self.assertEqual(self.response.status_code, 200)
    def test_diab_test_get(self):
        self.response=self.client.get(reverse('diab_test'))
        self.assertTemplateUsed(self.response,"diab_test.html")
        self.assertEqual(self.response.status_code, 200)
    def test_dia_admit_get(self):
        self.response=self.client.get(reverse('dia_admit'))
        self.assertTemplateUsed(self.response,"readmit.html")
        self.assertEqual(self.response.status_code, 200)
    def test_profile_get(self):
        self.response=self.client.get(reverse('profile'))
        self.assertTemplateUsed(self.response,"profile.html")
        self.assertEqual(self.response.status_code, 200)
