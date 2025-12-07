from django.db import models
from django.core.validators import MinLengthValidator

class task(models.Model):
    title = models.CharField(max_length=255, validators=[MinLengthValidator(1, message="Title not entered!")])
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255, validators=[MinLengthValidator(1, message="status not entered!")])
    dateTime = models.DateTimeField()