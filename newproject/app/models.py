from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser

class MyUser(AbstractBaseUser):
    pass
class teacher(models.Model):
    id_teacher = models.IntegerField(primary_key=10)
    username = models.CharField(null=False,max_length=255)
    password = models.CharField(max_length=255,null=False)
    fullname = models.CharField(null=False,max_length=255)
    faculty = models.CharField(null=True,max_length=255)
    branch = models.CharField(null=True, max_length=255)
    img= models.TextField(default='',null=True)
    def save(self, *args, **kwargs):
        if not self.pk or self._state.adding or self.password != self._old_password:
            self.password = make_password(self.password)
        super(teacher, self).save(*args, **kwargs)
    @property
    def _old_password(self):
        try:
            return teacher.objects.get(pk=self.pk).password
        except teacher.DoesNotExist:
            return None
class student(models.Model):
    id_student = models.IntegerField(primary_key=10)
    username = models.CharField(null=False,max_length=255)
    password = models.CharField(max_length=255,null=False)
    fullname = models.CharField(null=False,max_length=255)
    faculty = models.CharField(null=True,max_length=255)
    branch = models.CharField(null=True, max_length=255)
    img= models.TextField(default='',null=True)
    year = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.pk or self._state.adding or self.password != self._old_password:
            self.password = make_password(self.password)
        super(student, self).save(*args, **kwargs)
    @property
    def _old_password(self):
        try:
            return student.objects.get(pk=self.pk).password
        except student.DoesNotExist:
            return None

class project(models.Model):
    id_project = models.IntegerField(primary_key=10)
    id_student = models.ForeignKey(student, verbose_name="id_student", on_delete=models.CASCADE)
    id_teacher = models.ForeignKey(teacher, verbose_name="id_teacher", on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=255)

class faculty(models.Model):
    id_faculty = models.IntegerField(primary_key=10)
    name = models.CharField(null=False, max_length=255)

class branch(models.Model):
    id_branch = models.IntegerField(primary_key=10)
    name = models.CharField(null=False, max_length=255)

class file(models.Model):

    name = models.CharField(null=False, max_length=255)
    size = models.CharField(null=False, max_length=255)
    project_id = models.ForeignKey(project, verbose_name="id_project", on_delete=models.CASCADE)
