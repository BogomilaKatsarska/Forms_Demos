from django.core.exceptions import ValidationError
from django.db import models


def validate_name(value):
    first_last = value.split(' ')
    if len(first_last) != 2 :
        raise ValidationError('Name must include first and last name')


class Pet(models.Model):
    MAX_NAME_LEN = 30
    name = models.CharField(
        max_length=MAX_NAME_LEN,
    )

    def __str__(self):
        return self.name


class Person(models.Model):
    MAX_NAME_LEN = 30
    name = models.CharField(
        max_length=MAX_NAME_LEN,
        validators=(validate_name,),
    )
    age = models.PositiveIntegerField()

    pets = models.ManyToManyField(
        Pet,
    )