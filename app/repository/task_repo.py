from app.model.task import Task

class TaskRepository:
	def __init__(self, db):
		self._db = db

	def create(self, task):
		session = self._db.session
		session.add(task)
		session.commit()
		
	def get_by_id(self, id: int) -> Task:
		session = self._db.session
		task = session.query(Task).filter_by(id = id).first()
		return task
		
	def get_user_tasks(self, user_id: int):
		session = self._db.session
		tasks = session.query(Task).filter_by(user_id = user_id, is_completed=False).all()
		return tasks
		
	def save(self):
		self._db.session.commit()
