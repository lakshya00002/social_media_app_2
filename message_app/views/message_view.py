class MessageView:
    @staticmethod
    def render_message(message):
        return {
            "id": message.id,
            "sender_id": message.sender_id,
            "reciever_id": message.reciever_id,
            "timestamp": message.timestamp,
            "is_read": message.is_read,
            "content":message.content
        }

    @staticmethod
    def render_message(messages):
        return [MessageView.render_message(message) for message in messages]

    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, message_id=None):
        response = {"message": message}
        if message_id:
            response["message_id"] = message_id
        return response
