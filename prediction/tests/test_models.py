from django.test import TestCase
from prediction.models import Test,admit,users

class Testmodels(TestCase):
    def setup(self,User_Name='chinnu',Email="chinnu@gmail.com", Password='chinnu@123',):
        return users.objects.create(
            
            User_Name=User_Name,
            Email=Email,
        
            Password=Password
        )
    def test_users(self):
        u=self.setup()
        self.assertTrue(isinstance(u, users))
        self.assertEqual(u.__str__(), u.User_Name)
    def test_Test(self):
        u=self.setup()
        self.assertTrue(isinstance(u, users))
        self.assertEqual(u.__str__(), u.User_Name)
    def test_admit(self):
        u=self.setup()
        self.assertTrue(isinstance(u, users))
        self.assertEqual(u.__str__(), u.User_Name)