from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from ToDo.forms import ToDoForm
from ToDo.models import ToDo


class ToDoList(LoginRequiredMixin, generic.ListView):
    template_name = 'ToDo/todo_list.html'
    model = ToDo

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user).order_by('-modified')


class ToDoCreate(LoginRequiredMixin, generic.CreateView):
    template_name = 'ToDo/todo_create.html'
    form_class = ToDoForm

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.user = self.request.user
        todo.save()
        return redirect('todo-list')


class ToDoUpdate(LoginRequiredMixin, generic.UpdateView):
    template_name = 'ToDo/todo_update.html'
    form_class = ToDoForm

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user).order_by('-modified')

    def get_success_url(self):
        return reverse('todo-list')


class ToDoComplete(LoginRequiredMixin, generic.View):
    def get(self, request, pk):
        print(f'pk is: {pk}')
        todo = get_object_or_404(ToDo.objects.filter(user=request.user), pk=pk)
        print(todo)

        return redirect('todo-list')
