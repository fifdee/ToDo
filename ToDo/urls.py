from django.urls import path

from ToDo.views import ToDoList, ToDoCreate, ToDoUpdate, ToDoComplete

urlpatterns = [
    path('', ToDoList.as_view(), name='todo-list'),
    path('create/', ToDoCreate.as_view(), name='todo-create'),
    path('update/<int:pk>/', ToDoUpdate.as_view(), name='todo-update'),
    path('complete/<int:pk>/', ToDoComplete.as_view(), name='todo-complete'),
]