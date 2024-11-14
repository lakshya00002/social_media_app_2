from shared.models.messages_model import Message
from shared.models.user_model import User
from shared.utils.db_utils import db
from user_app.services.user_service import UserService
from notification_app.services.notification_service import NotificationService

class MessageServices:
    @staticmethod
    def send_message(sender_id,reciever_id,content):
        message=Message(sender_id=sender_id,reciever_id=reciever_id,content=content)
        db.session.add(message)
        db.sessin.commit()
        try:
          
            sender = User.query.get(sender_id)
            receiver = User.query.get(reciever_id)

            
            if sender and receiver:
                NotificationService.create_notification(
                    receiver.user_id, 
                    f"{sender.username} sent you a message"
                )

        except:
            db.session.rollback() 
                 


        return message

    @staticmethod
    def recieve_message(user_id):
        message=Message.query.filter((user_id==Message.sender_id)|(user_id==Message.reciever_id)).order_by(Message.timestamp.desc()).all()
        return message

    @staticmethod
    def mark_as_read(message_id):
        message=Message.query.filter(message_id)
        if message:
            message.is_read=True
            db.session.commit()
            return message
        return None
    
    @staticmethod
    def delete_message(message_id):
        message=Message.query.filter_by(id = message_id)
        if message:
            db.session.delete(message)
            db.session.commit()
            return True
        return False





