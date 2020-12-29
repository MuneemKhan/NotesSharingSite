from django.test import SimpleTestCase
from django.urls import reverse, resolve
from notes.views import userlogin, login_admin, signup1, admin_home, Logout, profile, edit_profile, changepassword, upload_notes, view_mynotes

class TestUrls(SimpleTestCase):

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, userlogin)

    def test_login_admin_url_is_resolved(self):
        url = reverse('login_admin')
        self.assertEquals(resolve(url).func, login_admin)

    def test_signup_url_is_resolved(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup1)

    def test_admin_home_url_is_resolved(self):
        url = reverse('admin_home')
        self.assertEquals(resolve(url).func, admin_home)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, Logout)

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_edit_profile_url_is_resolved(self):
        url = reverse('edit_profile')
        self.assertEquals(resolve(url).func, edit_profile)

    def test_changepassword_url_is_resolved(self):
        url = reverse('changepassword')
        self.assertEquals(resolve(url).func, changepassword)

    def test_upload_notes_url_is_resolved(self):
        url = reverse('upload_notes')
        self.assertEquals(resolve(url).func, upload_notes)

    def test_view_mynotes_url_is_resolved(self):
        url = reverse('view_mynotes')
        self.assertEquals(resolve(url).func, view_mynotes)