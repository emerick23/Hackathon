from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Job, Outcome, Contact
from .forms import OutcomeForm, StageForm, PrioritizeForm
# Create your views here.

def home(request):
    return render(request, 'home.html')
    LoginRequiredMixin, 
@login_required
def jobs_index(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request, 'jobs/index.html', {'jobs': jobs})

class JobCreate(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['company', 'position', 'company_address', 'prioritized', 'date_job_posted', 'types', 'job_url', 'date_applied', 'date_deadline', 'stage']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JobUpdate(LoginRequiredMixin, UpdateView):
    model = Job
    fields = ['company', 'position', 'company_address', 'prioritized', 'date_job_posted', 'types', 'job_url', 'date_applied', 'date_deadline', 'stage']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
class JobDelete(LoginRequiredMixin, DeleteView):
    model = Job
    success_url = '/jobs'

class ContactCreate(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['name', 'company', 'title', 'email']

    def form_valid(self, form):
        job = Job.objects.get(id=self.kwargs['job_id'])
        form.instance.user = self.request.user
        form.instance.job = job
        form.save()
        return redirect('jobs_detail', job_id=self.kwargs['job_id'])

class ContactDelete(LoginRequiredMixin, DeleteView):
    model = Contact
    success_url = '/jobs'

@login_required
def jobs_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    contact = job.contact_set.first()
    outcome_form = OutcomeForm()
    stage_form = StageForm()
    prioritize_form = PrioritizeForm()
    return render(request, 'jobs/detail.html', {'job': job, 'outcome_form': outcome_form, 'stage_form': stage_form, 'prioritize_form': prioritize_form, 'contact': contact})

@login_required
def job_prioritize(request, job_id):
    job = Job.objects.get(id=job_id)
    print(job.prioritized)
    if job.prioritized == 'F':
        job.prioritized = 'T'
        print(job.prioritized)
    else: 
        job.prioritized = 'F'
    job.save()
    return redirect('jobs_detail', job_id=job_id)

@login_required    
def stage_update(request, job_id):
    job = Job.objects.get(id=job_id)
    job.stage = request.POST['stage']
    job.save()
    return redirect('jobs_detail', job_id=job_id)

@login_required
def add_outcome(request, job_id):
    form = OutcomeForm(request.POST)
    if form.is_valid():
        new_outcome = form.save(commit=False)
        new_outcome.job_id = job_id
        new_outcome.save()
    return redirect('jobs_detail', job_id=job_id)

@login_required
def remove_outcome(request, job_id, outcome_id):
    outcome = Outcome.objects.get(id=outcome_id)
    outcome.delete()
    return redirect('jobs_detail', job_id=job_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

