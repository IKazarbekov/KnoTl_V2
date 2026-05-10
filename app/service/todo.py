from app.model import Task, User
from core.extensions import repo

def create(user: User, text: str):
	'''
	create task, send to data base throuth repo
	'''
	task = Task(user_id = user.id, text = text, is_completed = False)
	repo.tasks.create(task)

def get_all(user: User) -> list:
	'''
	get list from Tasks is not completed
	return: list from text and task id
	'''
	tasks = repo.tasks.get_user_tasks(user.id)
	
	task_texts = [(task.id, task.text) for task in tasks]

	return task_texts
	
def complete(task_id: int):
	task = repo.tasks.get_by_id(task_id)
	task.is_completed = True
	repo.tasks.save()
