from django.db import models
from django.contrib.auth.models import User


class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Semesters(models.Model):
    id = models.AutoField(primary_key=True)
    semester = models.CharField(max_length=50)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.semester + " " + self.course.name


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    semester = models.ForeignKey(Semesters, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.semester.semester


class Resources(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    sub = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    file = models.FileField(null=True)
    sem = models.ForeignKey(Semesters, on_delete=models.CASCADE, default=None)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class User_Requirements(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=20)
    resource = models.TextField()

    def __str__(self):
        return self.resource


class Feedbacks(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    feedback = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=60, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


