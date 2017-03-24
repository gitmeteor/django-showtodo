from django.shortcuts import render

# Create your views here.

from django.template import Context, loader
from django.views import generic
from todo.models import Task
from django.http import HttpResponse


class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'latest_task_list'

    def get_queryset(self):
        return Task.objects.order_by('-pub_date')[:5]

