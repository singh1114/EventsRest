from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class memorpart(models.Model):
    user = models.OneToOneField(
        User
    )
    memorpart = (
        ('Member', 'member'),
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

class Participant(models.Model):
    Participant_F_Name = models.CharField(
        max_length = 80,
        verbose_name = "Participant First Name",
    )
    Participant_L_Name = models.CharField(
        max_length = 80,
        verbose_name = "Participant Last Name",
    )
    Branches = (
        ('CSE', "Computer Science and Engineering"),
        ('IT', "Imformation Technology"),
        ('EE', "Electrical Engineering"),
        ('CE', "Civil Engineering"),
        ('ME', "Mechanical Engineering"),
        ('ECE', "Electronics and communication Engineering"),
        ('PE', "Production Engineering"),
    )
    Participant_Branch = models.CharField(
        max_length = 5,
        choices = Branches,
        verbose_name = "Participant Branch",
        default = 1
    )
    Year = (
        ('D1', 'D1'),
        ('D2', 'D2'),
        ('D3', 'D3'),
        ('D4', 'D4'),
    )
    Participant_Year = models.CharField(
        max_length = 3,
        choices = Year,
        verbose_name = 'Participant Year',
        default = 2
    )
    Participant_roll_number = models.IntegerField(
        verbose_name = "University Roll Number"
    )
    Participant_phone_number = models.CharField(
        max_length = 10,
        verbose_name = "Phone Number",
        default = 9098989898
    )
    Participant_email = models.EmailField(
        max_length = 40,
        verbose_name = "Email"
    )
