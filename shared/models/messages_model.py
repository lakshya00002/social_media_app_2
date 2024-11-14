from datetime import datetime
from shared.utils.db_utils import db

class Message(db.Model):
    __tablename__="messages"
    id=db.Column(db.Integer,primary_key=True)
    sender_id=db.Column(db.Integer,db.ForeignKey('users.user_id'),nullable=False)
    receiver_id=db.Column(db.Integer,db.ForeignKey('users.user_id'),nullable=False)
    content=db.Column(db.Text,nullable=False)
    timestamp=db.Column(db.DateTime,default=datetime.utcnow)
    is_read=db.Column(db.Boolean,default=False)


