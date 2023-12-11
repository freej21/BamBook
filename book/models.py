from django.db import models
import datetime
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.

class Visitor(models.Model):
    DEPARTMENT_CHOICES = (
        ('', 'Select a Department'),
        ('Engineering', 'Engineering'),
        ('Human Resources', 'Human Resources'),
        ('DPWH', 'DPWH'),
    )
    unique_id = models.CharField(editable=False, unique=True,blank=True, null=True, max_length=10)
    name = models.CharField(max_length=255)
    contact = models.BigIntegerField(null=True, blank=True)
    address = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    captured_photo = models.ImageField(upload_to='captured_visitor_photos/', blank=True, null=True)
    time_in = models.DateTimeField(default=timezone.now)
    time_out = models.DateTimeField(null=True, blank=True)
    department = models.CharField(
        max_length=20,
        choices=DEPARTMENT_CHOICES,
    )

    def __str__(self):
        return f"{self.name} - {self.unique_id}"
    date = models.DateField(null=True, blank=True, default=datetime.date.today)

    def __str__(self):
        return f"{self.name} - {self.unique_id}"

    def login(self):
        self.time_in = timezone.now()
        self.save()

    def logout(self):
        self.time_out = timezone.now()
        self.save()

    def calculate_stay_duration(self):
        if self.time_in and self.time_out:
            return self.time_out - self.time_in
        else:
            return None

    class Meta:
        ordering = ('-date',)


class Feedback(models.Model):
    visitor = models.ForeignKey('Visitor', on_delete=models.SET_NULL, null=True, blank=True)
    RATING_CHOICES = (
        (1, 'Strongly Disagree'),
        (2, 'Disagree'),
        (3, 'Neither Agree nor Disagree'),
        (4, 'Agree'),
        (5, 'Strongly Agree'),
        (0, 'N/A'),
    )
    item_1 = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)
    item_2 = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)
    item_3 = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)
    item_4 = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)
    item_5 = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)
    item_6 = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)
    item_7 = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)
    item_8 = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)
    item_9 = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)

    comment = models.TextField()
    
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-date_added',)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Recalculate and update AverageFeedback records
        for item_number in range(1, 10):
            average_rating = Feedback.objects.filter(visitor=self.visitor).aggregate(Avg(f'item_{item_number}'))[f'item_{item_number}__avg']
            average_feedback, created = AverageFeedback.objects.get_or_create(item_number=item_number)
            average_feedback.average_rating = average_rating or 0
            average_feedback.save()

@receiver(post_save, sender=Feedback)
def update_average_feedback(sender, instance, **kwargs):
    for item_number in range(1, 10):
        average_rating = Feedback.objects.filter(visitor=instance.visitor).aggregate(Avg(f'item_{item_number}'))[f'item_{item_number}__avg']
        average_feedback, created = AverageFeedback.objects.get_or_create(item_number=item_number)
        average_feedback.average_rating = average_rating or 0
        average_feedback.save()
        
        instance.visitor.logout()
class AverageFeedback(models.Model):
    item_number = models.IntegerField(unique=True)
    average_rating = models.FloatField(null=True)
    rating_description = models.CharField(max_length=50, null=True)

    class Meta:
        unique_together = ('item_number',)

    def determine_rating_description(self):
        if self.average_rating is None:
            return 'N/A'
        elif 1.0 <= self.average_rating <= 1.9:
            return 'Strongly Disagree'
        elif 2.0 <= self.average_rating <= 2.9:
            return 'Disagree'
        elif 3.0 <= self.average_rating <= 3.9:
            return 'Neither Agree nor Disagree'
        elif 4.0 <= self.average_rating <= 4.9:
            return 'Agree'
        elif self.average_rating == 5.0:
            return 'Strongly Agree'
        else:
            return 'Unknown'

    def save(self, *args, **kwargs):
        self.rating_description = self.determine_rating_description()
        super().save(*args, **kwargs)

