from django import forms

from ToDo.models import ToDo


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['description']