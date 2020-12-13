from django.test import SimpleTestCase
from django.urls import resolve,reverse
from prediction.views import signup,login,diab_test,home,dia_admit,profile,TestView
class Testurls(SimpleTestCase):
    def test_url_resolve_home(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func,home)
    def test_url_resolve_login(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func,login)
    def test_url_resolve_signup(self):
        url=reverse('signup')
        self.assertEquals(resolve(url).func,signup)
    def test_url_resolve_diab_test(self):
        url=reverse('diab_test')
        self.assertEquals(resolve(url).func,diab_test)
    def test_url_resolve_dia_admit(self):
        url=reverse('dia_admit')
        self.assertEquals(resolve(url).func,dia_admit)
    def test_url_resolve_profile(self):
        url=reverse('profile')
        self.assertEquals(resolve(url).func,profile)
   