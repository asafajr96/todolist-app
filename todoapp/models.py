from django.db import models

class ToDoApp(models.Model):
  added_date = models.DateTimeField()
  text = models.CharField(max_length = 255)