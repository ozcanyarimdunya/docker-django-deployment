from celery import states
from django.http import JsonResponse
from django.shortcuts import render

from celery.result import AsyncResult

from .tasks import task_demo
from .models import JobPool


def index(request):
    return render(request, 'hello/index.html')


def get_job_id(request, project_id=None):
    if not project_id:
        return JsonResponse({"data": "No project."})

    try:
        job_pool = JobPool.objects.get(project_id=project_id)
        job_id = job_pool.job_id
    except JobPool.DoesNotExist:
        return JsonResponse({"data": "No task."})

    return JsonResponse({"jobId": job_id})


def status(request, job_id=None):
    if not job_id:
        return JsonResponse({"data": "No task."})

    job = AsyncResult(str(job_id))

    if job.state == states.REVOKED:
        data = {
            "state": job.state,
            "result": 'terminated'
        }
    else:
        data = {
            "state": job.state,
            "result": job.result
        }

    return JsonResponse(data)


def start(request, project_id):
    if not project_id:
        return JsonResponse({"data": "No project."})

    duration = 10
    job = task_demo.delay(duration=duration)

    try:
        job_pool = JobPool.objects.get(project_id=project_id)
        job_pool.delete()
    except JobPool.DoesNotExist:
        pass

    JobPool.objects.create(
        job_id=job.id,
        project_id=project_id
    )

    return JsonResponse({"jobId": job.id})


def stop(request, project_id=None):
    if not project_id:
        return JsonResponse({"data": "No project."})

    try:
        job_pool = JobPool.objects.get(project_id=project_id)
        job_id = job_pool.job_id
    except JobPool.DoesNotExist:
        return JsonResponse({"data": "No task."})

    job = AsyncResult(str(job_id))
    job.revoke(terminate=True)

    return JsonResponse({"data": "Task stopped", "jobId": job_id})
