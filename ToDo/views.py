from django.shortcuts import render
from django.views import generic


class ToDoList(generic.TemplateView):
    template_name = 'ToDo/todo_list.html'
