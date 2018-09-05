from django.db import models


class JobPool(models.Model):
    job_id = models.UUIDField()
    project_id = models.IntegerField()
