from extensions import db

class TaskDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(280), nullable=False)
    priority = db.Column(db.String(40), nullable=False, default='high')
    category = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(80), nullable=False, default='To Do')