from flask import request ,jsonify
from message_app.services.message_service import MessageServices
from message_app.views.message_view import MessageView


class MessageController:
    @staticmethod
    def send_message(sender_id,reciever_id,content):
        message=MessageServices.send_message(sender_id,reciever_id,content)
        if message:
            return MessageView.render_message(message),201
        return MessageView.render_error("Failed to send message")

    @staticmethod
    def receive_message(user_id):
        message=MessageServices.receive_message(user_id)
        if message:
            return MessageView.render_message(message)
        return MessageView.render_error("No message found")
    
    @staticmethod
    def is_read(message_id):
        message=MessageServices.is_read(message_id)
        if message:
            return MessageView.render_message(message)
        return MessageView.render_error("Failed to mark as read")
    
    @staticmethod
    def delete_message(message_id):
        message=MessageServices.delete_message(message_id)
        if message:
            return MessageView.render_success("Message_deleted",message_id)
        return MessageView.render_error("Failed to delete message")