def in_progress(task_list):
    return sum(
        1 for task in task_list
        if task.status == "In Progress"
    )
