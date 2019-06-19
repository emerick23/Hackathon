from django.db import models
from django.urls import reverse
from datetime import datetime, date
from django.contrib.auth.models import User

# Create your models here.

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
    prioritized = models.BooleanField(default=False)
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

class Contact(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

class Outcome(models.Model):
    note = models.TextField(max_length=250)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

class Track(models.Model):
    research_company = models.BooleanField(default=True)
    research_position = models.BooleanField(default=False)
    contact_connection = models.BooleanField(default=False)
    customize_resume = models.BooleanField(default=False)
    customize_portfolio = models.BooleanField(default=False)
    customize_cover_letter = models.BooleanField(default=False)
    review_documents = models.BooleanField(default=False)
    email_checkin = models.BooleanField(default=False)
    research_job_interviewer = models.BooleanField(default=False)
    research_job_reqs = models.BooleanField(default=False)
    research_salary = models.BooleanField(default=False)
    practice_interview_questions = models.BooleanField(default=False)
    send_thanks = models.BooleanField(default=False)
    schedule_followup = models.BooleanField(default=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
