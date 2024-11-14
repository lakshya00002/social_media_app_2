from datetime import datetime
from shared.utils.db_utils import db

class Comment(db.Model):
    __tablename__="comments"
    comment_id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.Text,nullable=False)
    timestamp=db.Column(db.DateTime,default=datetime.utcnow)
    post_id=db.Column(db.Integer,db.ForeignKey('posts.post_id'),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('users.user_id'),nullable=False)