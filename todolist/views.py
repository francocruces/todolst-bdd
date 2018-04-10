from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from models import Task


def index(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        task = Task.objects.create(name=name)
    tasks = Task.objects.all()
    template = loader.get_template('index.html')
    context = {
        'tasks': tasks,
    }
    return HttpResponse(template.render(context, request))

