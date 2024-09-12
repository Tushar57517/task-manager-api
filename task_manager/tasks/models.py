from django.db import models
# from django.utils import timezone

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('done','Done'),
        ('pending', 'Pending'),
        ('in-progress','In Progress')
    ]

    PRIORITY_CHOICES = [
        ('high','High'),
        ('medium','Medium'),
        ('low','Low')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority= models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    due_date= models.DateField()
    created_date= models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title