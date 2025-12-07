from django.test import TestCase
from django import forms
from .models import task
import datetime
from django.core.exceptions import ValidationError
from django.urls import reverse

'''
def index(request):
    myTasks = task.objects.all().values()
    output = ""
    for x in myTasks:
        output += x["title"]
    return HttpResponse(output)
'''

class TaskTestCase(TestCase):

    #Test validation functions
    def test_create_task(self):
        title = "Read a book"
        description = "Better be a good one"
        status = "active"
        dateTime = datetime.datetime.now()
        ntask = task(title=title, description=description, status=status, dateTime=dateTime)
        try:
            ntask.full_clean()
            self.assertTrue(True)
        except ValidationError as e:
            self.assertTrue(False)

    def test_create_task_invalid_title_short(self):
        description = "Better be a good one"
        status = "active"
        dateTime = datetime.datetime.now()

        ntask = task(title="", description=description, status=status, dateTime=dateTime)
        try:
            ntask.full_clean()
            self.assertTrue(False)
        except ValidationError as e:
            self.assertTrue(True)

    def test_create_task_invalid_title_long(self):
        description = "Better be a good one"
        status = "active"
        dateTime = datetime.datetime.now()
        ntask = task(title="a"*300, description=description, status=status, dateTime=dateTime)
        try:
            ntask.full_clean()
            self.assertTrue(False)
        except ValidationError as e:
            self.assertTrue(True)

    def test_create_task_invalid_status_short(self):
        title = "Read a book"
        description = "Better be a good one"
        dateTime = datetime.datetime.now()

        ntask = task(title=title, description=description, status="", dateTime=dateTime)
        try:
            ntask.full_clean()
            self.assertTrue(False)
        except ValidationError as e:
            self.assertTrue(True)

    def test_create_task_invalid_status_long(self):
        title = "Read a book"
        description = "Better be a good one"
        dateTime = datetime.datetime.now()

        ntask = task(title=title, description=description, status="a"*300, dateTime=dateTime)
        try:
            ntask.full_clean()
            self.assertTrue(False)
        except ValidationError as e:
            self.assertTrue(True)


    #Test GET components
    def test_index_view(self):
        response = self.client.get("http://127.0.0.1:8000/")
        self.assertEqual(response.status_code, 200)

    def test_add_view(self):
        response = self.client.get("http://127.0.0.1:8000/add/")
        self.assertEqual(response.status_code, 200)


    #Test POST components
    def test_add_record_view(self):
        data = {"title": "Read a book", "description": "sfdsdf", "status": "Active", "dateTime": datetime.datetime.now()}
        response = self.client.post("http://127.0.0.1:8000/add/addrecord/", data)
        self.assertEqual(response.status_code, 302)

    
    def test_add_record_view_invalid(self):
        data = {"title": "", "description": "", "status": "", "dateTime": datetime.datetime.now()}
        response = self.client.post("http://127.0.0.1:8000/add/addrecord/", data)
        self.assertEqual(response.status_code, 400)