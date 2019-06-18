from django.contrib import admin
from .models import Job, Contact, Outcome

# Register your models here.
admin.site.register(Job)
admin.site.register(Contact)
admin.site.register(Outcome)
