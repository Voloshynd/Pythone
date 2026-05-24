from flask import Flask, render_template, request, redirect, jsonify
from datetime import datetime
from extensions import db
from Model import TaskDB
from load_tasks import load_tasks
from filter_tasks import filter_tasks
from digital_planner.services.completed_tasks import completed_tasks
from digital_planner.services.in_progress import in_progress
from digital_planner.services.overdue import overdue
from digital_planner.classes.Calendar import Calendar
from collections import defaultdict
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)

current_year = datetime.today().year


@app.route('/')
def home():
    task_list = load_tasks()
    completed = completed_tasks(task_list)
    progress = in_progress(task_list)
    passed = overdue(task_list)
    grouped_tasks = defaultdict(list)

    for task in task_list:
        grouped_tasks[task.date.date()].append(task)

    next_view = {
        "text": "Timieline",
        "url": "/calendar/"
    }

    return render_template(
        "list.html",
        next_view=next_view,
        task_list=task_list,
        task_len=len(task_list),
        grouped_tasks=grouped_tasks,
        completed=completed,
        progress=progress,
        passed=passed
    )


@app.route('/calendar/')
def calendar_view():
    task_list = load_tasks()
    completed = completed_tasks(task_list)
    progress = in_progress(task_list)
    passed = overdue(task_list)
    next_view = {
        "text": "List View",
        "url": "/list/"
    }

    calendar = Calendar(current_year, task_list)
    year_calendar = calendar.render_year()
    return render_template(
        "calendar.html",
        calendar=year_calendar,
        next_view=next_view,
        task_len=len(task_list),
        completed=completed,
        progress=progress,
        passed=passed
    )


@app.route('/list/')
def list_view():
    task_list = load_tasks()
    completed = completed_tasks(task_list)
    progress = in_progress(task_list)
    passed = overdue(task_list)

    grouped_tasks = defaultdict(list)

    for task in task_list:
        grouped_tasks[task.date.date()].append(task)

    next_view = {
        "text": "Year View",
        "url": "/year/"
    }

    return render_template(
        "list.html",
        next_view=next_view,
        task_list=task_list,
        grouped_tasks=grouped_tasks,
        task_len=len(task_list),
        completed=completed,
        progress=progress,
        passed=passed
    )


@app.route('/year/')
def year_view():
    task_list = load_tasks()
    completed = completed_tasks(task_list)
    progress = in_progress(task_list)
    passed = overdue(task_list)

    now = datetime.now()
    next_view = {
        "text": "Timeline",
        "url": "/calendar/"
    }

    return render_template(
        "task.html",
        next_view=next_view,
        task_list=task_list,
        task_len=len(task_list),
        completed=completed,
        progress=progress,
        passed=passed,
        now=now
    )


@app.route('/add/', methods=['GET', 'POST'])
def modal_view():
    error = ""
    link = ""

    if request.method == "POST":
        try:
            task = TaskDB(
                title=request.form["title"],
                description=request.form["description"],
                priority=request.form["priority"],
                category=request.form["category"],
                date=datetime.strptime(
                    request.form["due_date"],
                    "%Y-%m-%d"
                ).date()
            )

            db.session.add(task)
            db.session.commit()

            return redirect("/list/")

        except IntegrityError:
            db.session.rollback()
            error = "Task with this title already exists"

        except Exception as e:
            db.session.rollback()
            error = f"Unexpected error: {e}"

    previous_page = request.referrer or "/list/"

    if "/add/" in previous_page:
        link = "/list/"
    else:
        link = previous_page

    next_view = {
        "url": "/list/"
    }

    today = datetime.today().strftime('%Y-%m-%d')

    return render_template(
        "modal.html",
        next_view=next_view,
        link=link,
        today=today,
        error=error
    )


@app.route('/delete/<int:task_id>/')
def delete_task(task_id):
    task = db.session.query(TaskDB).filter(TaskDB.id == task_id).first()
    db.session.delete(task)
    db.session.commit()

    return redirect("/year/")


@app.route('/toggle/<int:task_id>/')
def toggle_status(task_id):
    task = db.session.query(TaskDB).filter(TaskDB.id == task_id).first()

    if task.status == "To Do":
        task.status = "In Progress"
    elif task.status == "In Progress":
        task.status = "Completed"
    else:
        task.status = "To Do"

    db.session.add(task)
    db.session.commit()

    previous_page = request.referrer
    link = previous_page.split("/")[-2]
    if link == "year":
        return redirect(previous_page + f"#task-{task_id}")
    else:
        return redirect(previous_page + f"#list-{task_id}")


@app.route('/search/', methods=["POST"])
def search_title():
    actual_page = request.referrer
    link = actual_page.split("/")[-2]

    if link == "calendar":
        return None
    else:
        data = request.get_json()
        query = data["search"].strip().lower()
        status = data["status"].lower()
        priority = data["priority"].lower()

        return jsonify({
            "redirect": f"/results?query={query}&status={status}&priority={priority}"})


@app.route("/results/")
def results():
    query = request.args.get("query", "")
    status = request.args.get("status", "")
    priority = request.args.get("priority", "")
    task_list = filter_tasks(query, status, priority)
    actual_page = request.referrer
    link = actual_page.split("/")[-2]
    now = datetime.now()
    completed = completed_tasks(task_list)
    progress = in_progress(task_list)
    passed = overdue(task_list)
    grouped_tasks = defaultdict(list)

    for task in task_list:
        grouped_tasks[task.date.date()].append(task)

    if link == "year":
        next_view = {
            "text": "Timeline",
            "url": "/calendar/"
        }
        return render_template(
            "task.html",
            task_list=task_list,
            task_len=len(task_list),
            completed=completed,
            progress=progress,
            passed=passed,
            next_view=next_view,
            now=now,
            query=query,
            status=status,
            priority=priority,
        )
    else:
        next_view = {
            "text": "Year View",
            "url": "/year/"
        }
        return render_template(
            "list.html",
            task_list=task_list,
            grouped_tasks=grouped_tasks,
            next_view=next_view,
            task_len=len(task_list),
            completed=completed,
            progress=progress,
            passed=passed,
            query=query,
            status=status,
            priority=priority
        )


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run()

# npx sass static/styles:static/css --watch
