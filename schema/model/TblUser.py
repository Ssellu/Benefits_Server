import datetime
from application import db


class User(db.Model):
    __tablename__ = "tbl_user"
    u_no = db.Column(db.Integer, primary_key=True)
    u_type = db.Column(db.Integer, default=0)
    u_email = db.Column(db.String, nullable=False, unique=True)
    u_password = db.Column(db.String, nullable=False)
    u_last_password = db.Column(db.DateTime, default=datetime.datetime.now())
    u_last_accessed = db.Column(db.DateTime, default=datetime.datetime.now())
    u_confirm = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, u_email, u_password):
        self.u_email = u_email
        self.u_password = u_password

    def __repr__(self):
        return '<email {}'.format(self.email)


