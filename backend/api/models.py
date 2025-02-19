import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    department = models.CharField(max_length=500)
    matricno = models.CharField(max_length=100, unique=True)
    level = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

class Document(models.Model):
    CATEGORY_CHOICES = [
        ('Academics', 'Academics'),
        ('Finance', 'Finance'),
        ('Accommodation', 'Accommodation'),
        ('Health', 'Health'),
        ('Administration', 'Administration'),
    ]
    
    STATUS_CHOICES = [
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Complete', 'Complete'),
        ('Incomplete', 'Incomplete'),
    ]
    
    document_name = models.CharField(max_length=255)
    document_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    document_status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    document_deadline = models.DateField()

    def __str__(self):
        return self.document_name

class Course(models.Model):
    course_title = models.CharField(max_length=255)
    course_code = models.CharField(max_length=10)
    course_unit = models.IntegerField()
    current_semester = models.CharField(max_length=20)
    level = models.IntegerField()
    course_venue = models.CharField(max_length=255)
    course_description = models.TextField()

    def __str__(self):
        return f"{self.course_code} - {self.course_title}"

class Resource(models.Model):
    CATEGORY_CHOICES = [
        ('Engineering', 'Engineering'),
        ('Science', 'Science'),
        ('Technology', 'Technology'),
        ('Mathematics', 'Mathematics'),
        ('General', 'General'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    articles = models.JSONField()  # Stores array of articles
    research_papers = models.JSONField()  # Stores array of research papers

    def __str__(self):
        return f"{self.category} Resources"

class Notification(models.Model):
    notification_date = models.DateField()
    notification_subject = models.CharField(max_length=255)
    notification_body = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.notification_subject

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    registered_courses = models.ManyToManyField(Course)
    total_units = models.IntegerField()
    level = models.IntegerField()
    about = models.TextField()
    department = models.CharField(max_length=100)
    matric_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"