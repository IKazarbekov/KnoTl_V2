import User

class TaskRepository:
	def __init__(self, db):
		self._db = db

	def createTask(self, user: User, text: str):
		from app.model.task import Task
		
		task = Task(user=user, text=text, is_completed=False)
		
		self._db.session.add(task)
		self._db.session.commit()
