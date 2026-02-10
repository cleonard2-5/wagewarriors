from django.contrib import admin

# Register your models here.
class messages(admin.ModelAdmin):
    idConvo = admin.IntegerField()
    recruiterIDFK = admin.IntegerField()
    jobSeekerIDFK = admin.IntegerField()
    message = admin.TextField()