from comment_app.services.comment_service import CommentService
from comment_app.views.comment_view import CommentView

class CommentController:
    @staticmethod
    def create_comment(user_id,post_id,content):
        comment=CommentService.create_comment(user_id,post_id,content)
        if comment:
            return CommentView.render_comment(comment)
        return CommentView.render_error("failed to create comment")
    
    @staticmethod
    def update_comment(comment_id,content):
        comment=CommentService.update_comment(comment_id,content)
        if comment:
            return CommentView.render_comment(comment)
        return CommentView.render_error("failed to update comment")
    
    @staticmethod
    def delete_comment(comment_id):
        comment=CommentService.delete_comment(comment_id)
        if comment:
            return CommentView.render_success("Comment deleted successfully",comment_id)
        return CommentView.render_error("failed to delete comment")
    
    


