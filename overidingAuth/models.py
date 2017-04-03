from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class memorpart(models.Model):
    user = models.OneToOneField(
        User
    )
    memorpart = (
        ('Member', "member"),
        ('Participant', "participant")
    )
    memorpart = models.CharField(
        max_length = 20,
        choices = memorpart,
        verbose_name = "Member or Participant",
        default = 1
    )

    def __str__(self):
        return self.user
