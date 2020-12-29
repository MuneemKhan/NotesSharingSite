from django.test import TestCase
from notes.models import Signup, Notes

class TestModels(TestCase):

    def setUp(self):
        self.project1 = Project.objects.create(
            name = 'Project 1'
        )

    def test_project_is_assigned_slug_on_creation(self):
        self.assertEquals(self.project1.slug, 'project 1')

    class Signup(models.Model):
        project = models.ForeignKey(Project, on_delete=models.CASCADE)
        name = models.CharField(max_length=50)

    class Notes(models.Model):
        project = models.ForeignKey(Project, on_delete=models.CASCADE)
        name = models.CharField(max_length=50)