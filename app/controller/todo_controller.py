from flask import Blueprint, redirect, request, url_for
from flask_login import login_required, current_user
from app.front import todo_page
from app.service import todo as service

todo_bp = Blueprint('todo', __name__, url_prefix='/todo')

@todo_bp.route('/')
@login_required
def root():
	user = current_user
	
	task_ids_and_texts = service.get_all(user)

	return todo_page.get(task_ids_and_texts)

@todo_bp.route('/add', methods=['POST'])
@login_required
def add():
	args = request.form
	text = args['tx']
	user = current_user
	
	service.create(user, text)
	
	return redirect('.')
	
@todo_bp.route('/cmp', methods=['GET'])
@login_required
def complete():
	args = request.args
	task_id = int(args['ok'])
	user = current_user
	
	service.complete(task_id)
	
	return redirect('.')
