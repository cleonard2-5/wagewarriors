from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from account.models import jobSeeker
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    if (not request.user.is_recruiter):
        return redirect('home.index')
    
    template_data = {}
    template_data['title'] = 'Applicants'
    applicantList = jobSeeker.objects.all()

    projects = request.GET.get('projects')
    location = request.GET.get('location')
    skill = request.GET.get('skill')
    
    if projects:
        applicantList = applicantList.filter(work_experience__icontains=projects)
    if location:
        applicantList = applicantList.filter(currentLocation__icontains=location)
    if skill:
        applicantList = applicantList.filter(skills__icontains=skill)

    template_data['applicants'] = applicantList

    return render(request, 'applicants/index.html', {'template_data': template_data})