from django.contrib import admin

from ToDo.models import ToDo, User

# Register your models here.
admin.site.register(ToDo)
admin.site.register(User)