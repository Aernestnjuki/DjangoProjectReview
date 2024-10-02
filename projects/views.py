from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

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


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {
        'form': form
    }
    return render(request, 'projects/project-form.html', context)

def updateProject(request, pk):
    one_project = Project.objects.get(id=pk)
    form = ProjectForm(instance=one_project)


    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=one_project)

        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        'form': form
    }

    return render(request, 'projects/update-form.html', context)

def deleteProject(request, pk):
    del_project = Project.objects.get(id=pk)

    if request.method == 'POST':
        del_project.delete()
        return redirect('projects')
    context = {
        'object': del_project
    }

    return render(request, 'projects/delete.html', context)
