from django.db import models
from django.core.validators import EmailValidator

class Person(models.Model):
    full_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    description = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        app_label = 'contactapp'
