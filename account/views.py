from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login # Alias to avoid name conflict
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SeekerSignupForm, RecruiterSignupForm
from .models import jobSeeker, recruiter, User
from django.contrib.auth import logout

# Create your views here.
#Landing page to let users sign up as a job seeker or recruiter
def index(request):
    template_data = {}
    template_data['title'] = 'Account'
    return render(request, 'account/index.html', {'template_data': template_data})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)

            if user.is_job_seeker:
                return redirect('account.profile', username=user.username)
            elif user.is_recruiter:
                return redirect('account.profile', username=user.username)
            else:
                return redirect('home.index')
        else:
            pass
    else:
        form = AuthenticationForm()
    

    return render(request, 'account/login.html', {'form': form})


# Loads user's profile
@login_required
def profile(request, username):
    template_data = {}
    template_data['title'] = 'Profile'
    user = get_object_or_404(User, username=username)
    return render(request, 'account/profile.html', {'template_data': template_data, 'user': user})

#logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect('home.index')

def seeker_signup(request):
    if request.method == 'POST':
        form = SeekerSignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_job_seeker = True
            user.save()
            jobSeeker.objects.create(user=user)
            return redirect('account.login') 
    else:
        form = SeekerSignupForm()
    
    return render(request, 'account/seeker_signup.html', {'form': form})
    
def recruiter_signup(request):
    if request.method == 'POST':
        form = RecruiterSignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_recruiter = True
            user.save()
            recruiter_profile = recruiter.objects.create(user=user)
            recruiter_profile.company_name = form.cleaned_data.get('company_name', '')
            recruiter_profile.save()
            return redirect('account.login')
    else:
        form = RecruiterSignupForm()
    
    return render(request, 'account/recruiter_signup.html', {'form': form})
