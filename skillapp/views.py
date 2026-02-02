from django.shortcuts import render
from .models import Skill

# Create your views here.

def skill_list():
    return Skill.objects.all()

