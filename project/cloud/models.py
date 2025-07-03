from django.db import models
from django.utils.translation import gettext_lazy

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)

    class Plan(models.IntegerChoices):
        HOBBY = 0, gettext_lazy("Hobby Plan")
        PRO = 1, gettext_lazy("Pro Plan")

    plan = models.IntegerField(default=Plan.HOBBY, choices=Plan.choices)


class App(models.Model):
    id = models.AutoField(primary_key=True)
    active = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Active(models.IntegerChoices):
        INACTIVE = 0, gettext_lazy("Inactive")
        ACTIVE = 1, gettext_lazy("Active")

    active = models.IntegerField(default=Active.INACTIVE, choices=Active.choices)
