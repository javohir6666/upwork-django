from django.db import models
from django.contrib.auth.models import AbstractUser
from config import settings
from datetime import datetime # idk if this is required, I assume so?
USER_TYPE = (
    ('Applicant', 'Applicant'),
    ('Employer', 'Employer'),
)

GENDER_SELECTION = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

LANGUAGES= (
    ('en', 'en'),
    ('ru', 'ru'),
    ('uz', 'uz'),
)

LEVEL_EDUCATION = (
    ('High school or equivalent', 'High school or equivalent'),
    ('Certification', 'Certification'),
    ('Vocational', 'Vocational'),
    ('Bachelor\'s deegree', 'Bachelor\'s deegree'),
    ('Master\'s deegree', 'Master\'s deegree'),
    ('Doctorate', 'Doctorate'),
)


class CustomUser(AbstractUser):
    user_type= models.CharField(max_length=20, choices=USER_TYPE)
    phone = models.CharField(max_length=17, blank=True, null=True)
    telegram = models.CharField(max_length=150, blank=True, null=True)
    instagram = models.CharField(max_length=150, blank=True, null=True)
    website = models.CharField(max_length=150, blank=True, null=True)
    linkedin= models.CharField(max_length=150, blank=True, null=True)
    facebook = models.CharField(max_length=150, blank=True, null=True)
    github = models.CharField(max_length=150, blank=True, null=True)
    youtube = models.CharField(max_length=150, blank=True, null=True)
    about = models.TextField(blank=True)
    languages = models.CharField(max_length=20, choices=LANGUAGES, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_SELECTION, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png', blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return str(self.username)


class Skill(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.title)

class WorkExperience(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.company)





class Education(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    name_of_deegree = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.title)
    
    def get_production_date(self):
        return self.start.strftime("%d-%m-%Y")
    
    def get_production_date(self):
        return self.end.strftime("%d-%m-%Y")