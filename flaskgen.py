import platform
from config import Config
from pathlib import Path
from shutil import copyfileobj
from argparse import ArgumentParser

if __name__ == "__main__":
	parser = ArgumentParser()
	parser.add_argument("project_name", help="Name of the root project folder")
	# Will be added later
	# parser.add_argument("--style", help="Defines the style of project and directory tree")
	args = parser.parse_args()

	project_style = 'elder'

	cwd = Path.cwd()
	project_tree = [
		Path(cwd, args.project_name),
		Path(cwd, args.project_name, 'application'),
		Path(cwd, args.project_name, 'application/routines'),
		Path(cwd, args.project_name, 'static'),
		Path(cwd, args.project_name, 'templates'),
		Path(cwd, args.project_name, 'testing')
	]

	try:
		for directory in project_tree:
			directory.mkdir()
	except:
		print("An error occured during creating project tree")

	template_code = Path(Config.FLASKGEN_PATH, 'tpl', project_style)
	file_mapping = {
		"app_config.py.tpl": Path(cwd, args.project_name, 'application/config.py'),
		"app_init.py.tpl": Path(cwd, args.project_name, 'application/__init__.py'),
		"app_rou_init.py.tpl": Path(cwd, args.project_name, 'application/routines/__init__.py'),
		"app_rou_models.py.tpl": Path(cwd, args.project_name, 'application/routines/models.py'),
		"app_rou_views.py.tpl": Path(cwd, args.project_name, 'application/routines/views.py'),
		"app_wsgi_app.py.tpl": Path(cwd, args.project_name, 'application/wsgi_app.py'),
		"main_script.py.tpl": Path(cwd, args.project_name, args.project_name + '.py'),
		"tem_index.html.tpl": Path(cwd, args.project_name, 'templates/index.html'),
		"tem_user.html.tpl": Path(cwd, args.project_name, 'templates/user.html')
	}

	try:
		for src, dst_path in file_mapping.items():
			src_path = Path(template_code, src)
			src_file = src_path.open('rb')
			dst_file = dst_path.open('wb')
			copyfileobj(src_file, dst_file, length=1024)
			src_file.close()
			dst_file.close()
	except Exception as e:
		print("An error occured during copying project files")
