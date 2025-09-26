from django.db import models

# Create your models here.
class Event(models.Model):
    CATEGORY = [
        ("Social", "Social"),
        ("Workshop", "Workshop"),
        ("Meetup", "Meetup"),
        ("Conference", "Conference"),
        ("Other", "Other"),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY)

    def __str__(self):
        return self.title