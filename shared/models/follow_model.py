from datetime import datetime
from shared.utils.db_utils import db

class Follow(db.Model):
    __tablename__='follwers'
    id=db.Column(db.Integer,primary_key=True)
    follower_username=db.Column(db.Integer,db.ForeignKey('users.username'),nullable=True)
    followee_username=db.Column(db.Integer,db.ForeignKey('users.username'),nullable=True)
    timestamp=db.Column(db.DateTime,default=datetime.utcnow)
    