from django.test import TestCase, Client
from django.urls import reverse
from notes.models import Signup, Notes
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.login_admin_url = reverse('login_admin')
        self.signup_url = reverse('signup')
        self.admin_home_url = reverse('admin_home')
        self.logout_url = reverse('logout')
        self.profile_url = reverse('profile')
        self.edit_profile_url = reverse('edit_profile')
        self.changepassword_url = reverse('changepassword')
        self.upload_notes_url = reverse('upload_notes')
        self.view_mynotes_url = reverse('view_mynotes')

    def test_userlogin_GET(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/templates/login.html')

    def test_login_admin_GET(self):
        response = self.client.get(self.login_admin_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/templates/login_admin.html')

    def test_signup1_GET(self):
        response = self.client.get(self.signup_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/templates/signup.html')

    def test_admin_home_GET(self):
        response = self.client.get(self.admin_home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/templates/admin_home.html')

    def test_Logout_GET(self):
        response = self.client.get(self.logout_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/templates/index.html')

    def test_profile_GET(self):
        response = self.client.get(self.profile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/templates/profile.html')

    def test_edit_profile_GET(self):
        response = self.client.get(self.edit_profile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/templates/edit_profile.html')

    def test_changepassword_GET(self):
        response = self.client.get(self.changepassword_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/templates/changepassword.html')

    def test_upload_notes_GET(self):
        response = self.client.get(self.upload_notes_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/templates/upload_notes.html')

    def test_view_mynotes_GET(self):
        response = self.client.get(self.view_mynotes_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/templates/view_mynotes.html')