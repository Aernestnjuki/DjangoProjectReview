from django.shortcuts import render
from .models import Project

# Create your views here.

def projects(request):
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects
    }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    one_project = Project.objects.get(id=pk)

    # getting the project tags
    tags = one_project.tags.all()

    # getting the review
    reviews = one_project.review_set.all()

    context = {
        'project': one_project,
        'tags': tags,
        'reviews': reviews
    }
    return render(request, 'projects/singleProject.html', context)
