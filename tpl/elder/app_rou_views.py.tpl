from application.wsgi_app import app
from application.routines.models import User
from flask import render_template, redirect, url_for


@app.route('/', methods=('GET',))
def index():
	return render_template('index.html')


@app.route('/user/<int:user_id>', methods=('GET',))
def user(user_id):
	user = User.query.filter_by(user_id=user_id).one_or_none()
	if not user:
		return redirect(url_for('index'))

	return render_template('user.html', username=user.name)