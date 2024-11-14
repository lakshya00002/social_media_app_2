from datetime import datetime
from shared.utils.db_utils import db

class Notification(db.Model):
    __table__name = 'notifications'

    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('users.user_id'),nullable=False)
    message=db.Column(db.Text,nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)
    read=db.Column(db.Boolean,default=False)