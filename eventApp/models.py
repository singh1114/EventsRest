from django.db import models

# Create your models here.
class EventList(models.Model):
    Event_Id = models.AutoField(
        primary_key = True,
        verbose_name = "Event ID",
    )
    Event_Name = models.CharField(
        max_length = 100,
        verbose_name = "Event Name",
    )
    Event_Venue = models.CharField(
        max_length = 10,
        verbose_name = "Event Venue",
    )
    Event_Start_time = models.DateTimeField(
        verbose_name = "Event starting time",
    )
    Event_End_time = models.DateTimeField(
        verbose_name = "Event ending time",
    )

    def __str__(self):
        return self.Event_Name

class MemberList(models.Model):
    Event_Id = models.ForeignKey(
        EventList,
        on_delete = models.CASCADE,
    )
    Member_Name = models.CharField(
        max_length = 80,
        verbose_name = "Member Name",
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
    Member_Branches = models.CharField(
        max_length = 5,
        choices = Branches,
        verbose_name = "Member Branch",
        default = 1
    )
    Year = (
        ('D1', 'D1'),
        ('D2', 'D2'),
        ('D3', 'D3'),
        ('D4', 'D4'),
    )
    Member_Year = models.CharField(
        max_length = 3,
        choices = Year,
        verbose_name = 'Member Year',
        default = 2
    )
    Member_roll_number = models.IntegerField(
        verbose_name = "University Roll Number"
    )
    Member_phone_number = models.CharField(
        max_length = 10,
        verbose_name = "Phone Number",
        default = 9098989898
    )
    Member_email = models.EmailField(
        max_length = 40,
        verbose_name = "Email"
    )

class ParticipantsList(models.Model):
    Event_Id = models.ForeignKey(
        EventList,
        on_delete = models.CASCADE,
    )
    Participants_Name = models.CharField(
        max_length = 80,
        verbose_name = "Participants Name",
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
    Participants_Branches = models.CharField(
        max_length = 5,
        choices = Branches,
        verbose_name = "Participants Branch",
        default = 1
    )
    Year = (
        ('D1', 'D1'),
        ('D2', 'D2'),
        ('D3', 'D3'),
        ('D4', 'D4'),
    )
    Participants_Year = models.CharField(
        max_length = 3,
        choices = Year,
        verbose_name = 'Participants Year',
        default = 2
    )
    Participants_roll_number = models.IntegerField(
        verbose_name = "University Roll Number"
    )
    Participants_phone_number = models.CharField(
        max_length = 10,
        verbose_name = "Phone Number",
        default = 9098989898
    )
    Participants_email = models.EmailField(
        max_length = 40,
        verbose_name = "Email"
    )
