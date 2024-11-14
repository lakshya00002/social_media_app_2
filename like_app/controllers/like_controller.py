from like_app.services.like_service import LikeService
from like_app.views.like_view import LikeView

class LikeController:
    @staticmethod
    def create_like(user_id,post_id):
        like=LikeService.create_like(user_id,post_id)
        if like:
            return LikeView.render_like(like)
        return LikeView.render_error("Failed to like")
    
    @staticmethod
    def delete_like(like_id):
        like=LikeService.delete_like(like_id)
        if like:
            return LikeView.render_like(like)
        return LikeView.render_error("failed to delete like")
    
    
