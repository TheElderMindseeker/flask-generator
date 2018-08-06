from application.wsgi_app import db


class User(db.Model):
	__tablename__ = 'user'

	user_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), nullable=False)