from core.extensions import db
from app.model import Task, User

def create(user: User, text: str):
	'''
	create task, send to data base throuth repo
	'''
	
	task = Task(user_id = user.id, text = text, is_completed = False)
	
	session = db.session
	session.add(task)
	session.commit()

def get_all(user: User) -> list:
	'''
	get list from Tasks is not completed
	return: list from text and task id
	'''
	tasks = db.session.query(Task).filter_by(user_id=user.id).all()
	
	task_texts = [(task.id, task.text) for task in tasks]
	
	return task_texts
