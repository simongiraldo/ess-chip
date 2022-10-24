from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, blank=False)
    saldo = models.CharField(max_length=5, blank=True)
    bloqueado = models.BooleanField(blank=True, default=False)
    carrera = models.CharField(max_length=50, blank=True)
    semestre = models.CharField(max_length=2, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username