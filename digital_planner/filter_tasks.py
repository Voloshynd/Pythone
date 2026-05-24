from Model import TaskDB
from digital_planner.classes.Task import Task
from extensions import db

def filter_tasks(query="", status="all", priority="all"):
    q = db.session.query(TaskDB)

    if query:
        q = q.filter(TaskDB.title.ilike(f"%{query}%"))

    if status and status != "all":
        q = q.filter(TaskDB.status.ilike(status))

    if priority and priority != "all":
        q = q.filter(TaskDB.priority.ilike(priority))

    tasks = q.all()

    return [
        Task(
            task.id,
            task.title,
            task.description,
            task.priority,
            task.category,
            task.date,
            task.status
        )
        for task in tasks
    ]