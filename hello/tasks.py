from time import sleep

from celery import shared_task, current_task


@shared_task
def task_demo(duration: int = 10):
    current_task.update_state(state="PROGRESS", meta={"operation": "start"})

    for _ in range(duration):
        sleep(_)
        current_task.update_state(state="PROGRESS", meta={"operation": "in-for-loop"})

    current_task.update_state(state="PROGRESS", meta={"operation": "finished"})
    return {"operation": "finished"}
