from flask import Blueprint,jsonify,request
from message_app.controllers.message_controller import MessageController

message_bp = Blueprint('message_bp',__name__)

@message_bp.route('/messages/send',methods=['POST'])
def send_message():
    data = request.get_json()
    sender_id=data.get('sender_id')
    reciever_id=data.get('reciever_id')
    content=data.get('content')
    
    if not sender_id or not reciever_id or not content:
        return {"error":"Missing required files"}
    return MessageController.send_message(sender_id,reciever_id,content)

@message_bp.route('/message/<int:user_id>',methods=['GET'])
def receive_message(user_id):
    return MessageController.receive_message(user_id)

@message_bp.route('/messages/<int:message_id>',methods=['PUT'])
def is_read(message_id):
    return MessageController.is_read(message_id)

@message_bp.route('/messages/<int:message_id>',methods=['DELETE'])
def delete_message(message_id):
    return MessageController.delete_message(message_id)



