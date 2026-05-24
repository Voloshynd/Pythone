from datetime import datetime

def overdue(task_list):
    today = datetime.now().date()

    return sum(
        1 for task in task_list
        if task.date.date() < today
    )
