from django.db import models

# Create your models here.
class jobSeeker(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    headline = models.CharField(max_length=255, blank=True)
    skills = models.TextField(blank=True)
    education = models.TextField(blank=True)
    work_experience = models.TextField(blank=True)
    additional_links = models.TextField(blank=True)
    isPrivate = models.BooleanField(default=False)
    currentLocation = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name


class recruiter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255, blank=True)
    isAdmin = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class jobsAppliedTo(models.Model):
    jobIDFK = models.IntegerField()
    jobSeekerIDFK = models.IntegerField()
    note = models.TextField(blank=True)
    status = models.enums.TextChoices('Applied', 'Review', 'Interview', 'Offer', 'Closed', 'Rejected', name='application_status')