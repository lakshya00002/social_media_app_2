from follow_app.services.follow_service import FollowService
from follow_app.views.follower_view import FollowerView

class FollowController:
    @staticmethod
    def follow(follower_username,followee_username):
        follow=FollowService.follow(follower_username,followee_username)
        if follow:
            return FollowerView.render_follow(follow)
        return FollowerView.render_error("failed to follow user")
    
    @staticmethod
    def unfollow(follower_username,followee_username):
        unfollow=FollowerView.unfollow(follower_username,followee_username)
        if unfollow:
            return FollowerView.render_follow(unfollow)
        return FollowerView.render_error("failed to unfollow user")