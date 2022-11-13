from django.urls import path

from ToDo.views import ToDoList, ToDoCreate, ToDoUpdate, ToDoComplete, ToDoListCompleted, ToDoDelete

urlpatterns = [
    path('', ToDoList.as_view(), name='todo-list'),
    path('completed/', ToDoListCompleted.as_view(), name='todo-list-completed'),
    path('create/', ToDoCreate.as_view(), name='todo-create'),
    path('update/<int:pk>/', ToDoUpdate.as_view(), name='todo-update'),
    path('complete/<int:pk>/', ToDoComplete.as_view(), name='todo-complete'),
    path('delete/<int:pk>/', ToDoDelete.as_view(), name='todo-delete'),
]