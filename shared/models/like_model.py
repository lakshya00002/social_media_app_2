from datetime import datetime
from shared.utils.db_utils import db

class Like(db.Model):
    __tablename__='likes'
    like_id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('users.user_id'),nullable=False)
    post_id=db.Column(db.Integer,db.ForeignKey('posts.post_id'),nullable=False)


class Dislike(db.Model):
    __tablename__='dislikes'
    deslike_id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('users.user_id'),nullable=False)
    post_id=db.Column(db.Integer,db.ForeignKey('posts.post_id'),nullable=False)  