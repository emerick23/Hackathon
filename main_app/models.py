from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

TYPES = (
    ('I', 'Internship'),
    ('C', 'Contract'),
    ('P', 'Part-Time'),
    ('F', 'Full-Time'),
)

class Job(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    company_address = models.CharField(max_length=100)
    notes = models.TextField(max_length=250)
    types = models.CharField(
        max_length=1,
        choices=TYPES,
        default=TYPES[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('jobs_detail', kwargs={'job_id': self.id})

