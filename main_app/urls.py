from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.jobs_index, name='jobs_index'),
    path('jobs/create/', views.JobCreate.as_view(), name='jobs_create'),
    path('jobs/<int:job_id>/', views.jobs_detail, name='jobs_detail'),
    path('jobs/<int:pk>/update', views.JobUpdate.as_view(), name='jobs_update'),
    path('jobs/<int:pk>/delete', views.JobDelete.as_view(), name='jobs_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]