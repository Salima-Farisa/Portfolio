from django.shortcuts import render
from .models import Profile
from skillapp.models import Skill
from experienceapp.models import Experience
from projectapp.models import Project

# Create your views here.

def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    experiences = Experience.objects.order_by('-start_date')
    projects = Project.objects.all().order_by('-created_at')

    return render(request, "home.html", {
        "profile": profile,
        "skills": skills,
        "experiences": experiences,
        "projects" : projects
    })
