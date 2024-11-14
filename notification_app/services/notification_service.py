from shared.models.notification_model import Notification
from shared.utils.db_utils import db

class NotificationService:
    @staticmethod
    def create_notification(user_id, message):
        notification =Notification(user_id=user_id, message=message)
        db.session.add(notification)
        db.session.commit()
        return notification
    
    @staticmethod
    def get_notification(user_id):
        return Notification.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def mark_as_read(notification_id):
        notification = Notification.query.get(notification_id)
        if notification:
            notification.read=True
            db.session.commit
        return notification
    
   
    