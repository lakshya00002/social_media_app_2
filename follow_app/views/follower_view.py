class FollowerView:
    @staticmethod
    def render_message(follower):
        return {
            "follwer_username": follower.follower_username,
            "followee_username": follower.followee_username,
            
        }

    @staticmethod
    def render_follow(followers):
        return [FollowerView.render_message(follower) for follower in followers]

    @staticmethod
    def render_error(error_message):
        return {"error": error_message}

    @staticmethod
    def render_success(success_message, follower_id=None):
        response = {"message": success_message}
        if follower_id:
            response["follower_id"] = follower_id
        return response