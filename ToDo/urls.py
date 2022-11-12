from django.urls import path

from ToDo.views import ToDoList

urlpatterns = [
    path('', ToDoList.as_view(), name='todo-list'),
]