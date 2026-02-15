from django.db import models

# Create your models here.
class job(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    skills= models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    salaryLower = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salaryUpper = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    isRemote = models.BooleanField(default=False)
    hasVisaSponsorship = models.BooleanField(default=False)
    company = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title}: {self.id}"   