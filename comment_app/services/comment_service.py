from datetime import datetime
from shared.models.comment_model import Comment
from shared.utils.db_utils import db
from notification_app.services.notification_service import NotificationService
from shared.models.post_model import Post

class CommentService:
    @staticmethod
    def create_comment(user_id,post_id,content):
        comment = Comment(user_id=user_id,post_id=post_id,content=content)
        db.session.add(comment)
        db.session.commit()
        
        try:
            post = Post.query.filter.get_post_by_id(post_id)
            NotificationService.create_notification(post.user_id,"Your post recieved a comment from{UserService.get_user_by_id(user_id)}")
        except:
            db.session.rollback()
        
    
        return comment
    
    @staticmethod
    def update_comment(comment_id,content):
        comment=Comment.query.filter(comment_id=comment_id).first()
        if comment:
            comment.content =content
            comment.timestamp = datetime.utcnow
            db.session.commit()
        return comment

    @staticmethod
    def delete_comment(comment_id):
        comment=Comment.query.filter(comment_id=comment_id).first()
        if comment:
            db.session.delete(comment)
            db.session.commit
        return comment        
        

        
