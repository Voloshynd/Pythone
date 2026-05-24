from Model import TaskDB
from digital_planner.classes.Task import Task
from extensions import db

def load_tasks():

    task_list = []

    for task in db.session.query(TaskDB).all():
        task_list.append(
            Task(
                task.id,
                task.title,
                task.description,
                task.priority,
                task.category,
                task.date,
                task.status
            )
        )

    return task_list

