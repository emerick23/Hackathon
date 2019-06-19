from django.forms import ModelForm 
from .models import Outcome, Track

class OutcomeForm(ModelForm):
    class Meta:
        model = Outcome
        fields = ['note']

class TrackForm(ModelForm):
    class Meta:
        model = Track
        fields = ['research_company', 'research_position', 'contact_connection', 'customize_resume', 'customize_portfolio', 'customize_cover_letter', 'review_documents', 'email_checkin', 'research_job_interviewer', 'research_job_reqs', 'research_salary', 'practice_interview_questions', 'send_thanks', 'schedule_followup']