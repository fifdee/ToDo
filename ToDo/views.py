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
        return ToDo.objects.filter(user=self.request.user, completed=False).order_by('-modified')


class ToDoListCompleted(LoginRequiredMixin, generic.ListView):
    template_name = 'ToDo/todo_list.html'
    model = ToDo

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user, completed=True).order_by('-modified')

    def get_context_data(self, *args, **kwargs):
        context = super(ToDoListCompleted, self).get_context_data(*args, **kwargs)
        context['completed'] = True
        return context


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
    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        todo = get_object_or_404(ToDo.objects.filter(user=request.user), pk=pk)
        todo.completed = True
        todo.save()

        return redirect('todo-list')


class ToDoDelete(LoginRequiredMixin, generic.View):
    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        todo = get_object_or_404(ToDo.objects.filter(user=request.user), pk=pk)
        todo.delete()

        return redirect('todo-list-completed')