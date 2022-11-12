from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


def user_created(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(user_created, sender=User)
