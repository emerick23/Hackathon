from django.db import models
from django.urls import reverse
from datetime import datetime, date
from django.contrib.auth.models import User

# Create your models here.
BOOLS = (
    ('T', 'True'),
    ('F', 'False')
)

TYPES = (
    ('I', 'Internship'),
    ('C', 'Contract'),
    ('P', 'Part-Time'),
    ('F', 'Full-Time'),
)

STAGES = (
    ('A', 'Apply'),
    ('I', 'Interview'),
    ('F', 'Follow Up'),
    ('O', 'Outcomes'),
)

class Job(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    prioritized = models.CharField(
        max_length=1,
        choices=BOOLS,
        default=BOOLS[0][0]
    )
    date_job_posted = models.DateField(default=date.today)
    types = models.CharField(
        max_length=1,
        choices=TYPES,
        default=TYPES[0][0]
    )
    job_url = models.CharField(max_length=100)
    date_applied = models.DateField(default=date.today)
    date_deadline = models.DateField(default=date.today)
    date_updated = models.DateTimeField(auto_now=True)
    stage = models.CharField(
        max_length=1,
        choices=STAGES,
        default=STAGES[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('jobs_detail', kwargs={'job_id': self.id})

    def prioritize(self):
        print('hello')

class Contact(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

class Outcome(models.Model):
    note = models.TextField(max_length=250)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)