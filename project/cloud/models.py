from django.db import models
from django.utils.translation import gettext_lazy

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)

    class Plan(models.IntegerChoices):
        HOBBY = 0, gettext_lazy("Hobby Plan")
        PRO = 1, gettext_lazy("Pro Plan")

    plan = models.CharField(
        default="hobby", choices=(("hobby", "Hobby plan"), ("pro", "Pro plan"))
    )


class App(models.Model):
    id = models.AutoField(primary_key=True)
    active = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    active = models.CharField(
        default="active",
        choices=(("inactive", "Inactive app"), ("active", "Active app")),
    )
