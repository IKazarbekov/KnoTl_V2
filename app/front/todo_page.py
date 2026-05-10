from app.front.page_builder import *

def get(task_ids_and_texts: list):
	'''
	param: task_texts : list from task id and task text
	'''
	
	page_objs = []
	for id, text in task_ids_and_texts:
		page_objs.append(
			[
				Label(f'{id}:{text} '),
				Url('ok', f'cmp?ok={id}')
			]
		)
	page_objs.append(UrlCard('Создать задачу','c'))
	
	page = create_page(
		[
			Card('Задачник', page_objs, id='m'),
			Card('Создать задачу', [
				Form([
					[
						Label('Описание'),
						TextBox('tx')
					]
				], url='add', is_post_method=True),
				UrlCard('назад','m')
			], id='c'),
		],
		False
	)
	
	return page
