from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import task
from django.urls import reverse
import datetime
from django.core.exceptions import ValidationError
from django.contrib import messages


#Displays all tasks
def index(request):
    mytasks = task.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mytasks': mytasks,
    }
    return HttpResponse(template.render(context, request))

#Link to add page
def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

#POST new task
def addrecord(request):
    title = request.POST['title']
    description = request.POST['description']
    status = request.POST['status']
    dateTime = request.POST['dateTime']

    ntask = task(title=title, description=description, status=status, dateTime=dateTime)
    try:
        ntask.full_clean()
    except ValidationError as e:
        print(next(iter(e.message_dict)), e.message_dict[next(iter(e.message_dict))][0])
        error = str(next(iter(e.message_dict))) + ":" + e.message_dict[next(iter(e.message_dict))][0]
        response = f"""
        <script>
            alert("Error in {error}");
            window.history.back();
        </script>
        """
        return HttpResponse(response,
        status=400)
    ntask.save()
    return HttpResponseRedirect(reverse('index'))