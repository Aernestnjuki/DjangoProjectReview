from django.shortcuts import render

# Create your views here.


jobs = [
    {
        'id': '1',
        'title': 'React.js developer',
        'description': 'You will create user oriented front end apps'
    },
    {
        'id': '2',
        'title': 'Django developer',
        'description': 'You will create backend with Django'
    },
    {
        'id': '3',
        'title': 'Flask developer',
        'description': 'You will create backend with flask'
    },
    {
        'id': '4',
        'title': 'Node.js developer',
        'description': 'You will create websites with node'
    },
]

def projects(request):
    context = {
        'jobs': jobs
    }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    jobObj = None

    for i in jobs:
        if i['id'] == str(pk):
            jobObj = i

    context = {
        'job': jobObj
    }
    return render(request, 'projects/singleProject.html', context)
