from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save, pre_save


class User(AbstractUser):
    pass


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


def set_username(sender, instance, **kwargs):
    email = instance.email
    username = email[:30]
    n = 1
    while User.objects.exclude(pk=instance.pk).filter(username=username).exists():
        n += 1
        username = email[:(29 - len(str(n)))] + '-' + str(n)
    instance.username = username


pre_save.connect(set_username, sender=User)
