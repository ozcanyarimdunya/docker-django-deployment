from django.urls import path
from .views import (
    index,
    get_job_id,
    start,
    status,
    stop
)

app_name = "hello"
urlpatterns = [
    path('', index, name="index"),
    path('get-job-id/<int:project_id>/', get_job_id, name="get-job-id"),
    path('start/<int:project_id>/', start, name="start"),
    path('status/<uuid:job_id>/', status, name="status"),
    path('stop/<int:project_id>/', stop, name="stop"),
]
