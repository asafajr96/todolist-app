from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import ToDoApp
from django.http import HttpResponseRedirect



def index(request):
  to_do_list = ToDoApp.objects.all().order_by("-added_date")
  return render(request,"index.html", {"to_do_list": to_do_list})

@csrf_exempt
def add_item(request):
  date_added = timezone.now()
  content = request.POST["content"]
  ToDoApp.objects.create(added_date=date_added, text=content)
  return HttpResponseRedirect("/")

@csrf_exempt
def delete_item(request, todo_id):
  ToDoApp.objects.get(id=todo_id).delete()
  return HttpResponseRedirect("/")
