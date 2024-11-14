class LikeView:
    @staticmethod
    def render_message(like):
        return {
            "like_id": like.like_id,
            "user_id":like.user_id,
            "post_id":like.post_id

        }

    @staticmethod
    def render_like(likes):
        return [LikeView.render_message(like) for like in likes]

    @staticmethod
    def render_error(error_message):
        return {"error": error_message}

    @staticmethod
    def render_success(success_message, like_id=None):
        response = {"message": success_message}
        if like_id:
            response["like_id"] = like_id
        return response