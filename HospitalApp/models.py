"""A model is the single, definitive source of information
about your data. It contains the essential fields and behaviors
of the data you’re storing. Generally, each model maps to a single
database table.

The basics:

- Each model is a Python class that subclasses django.db.models.Model.
- Each attribute of the model represents a database field.
- With all of this, Django gives you an automatically-generated
database-access API; see Making queries."""

from django.db import models
from django.contrib.auth.models import User
# Esa clas User es la que conecta a la tabla de auth_user



# Create your models here.
class perfilOperario(models.Model):
    operario = models.OneToOneField(User,models.CASCADE)
    empresa = models.CharField(max_length=50, default='')
    nombre = models.CharField(max_length=50, default='')
    telefono = models.BigIntegerField(default=0)


