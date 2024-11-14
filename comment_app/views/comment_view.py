class CommentView:
    @staticmethod
    def render_message(comment):
        return {
            "comment_id": comment.id,
            "user_id": comment.sender_id,
            "timestamp": comment.timestamp,
            "content":comment.content,
            "post_id":comment.post_id

        }

    @staticmethod
    def render_comment(comments):
        return [CommentView.render_message(comment) for comment in comments]

    @staticmethod
    def render_error(error_message):
        return {"error": error_message}

    @staticmethod
    def render_success(success_message, comment_id=None):
        response = {"message": success_message}
        if comment_id:
            response["comment_id"] = comment_id
        return response