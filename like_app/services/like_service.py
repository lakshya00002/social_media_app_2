from datetime import datetime
from shared.utils.db_utils import db
from shared.models.like_model import Like
from shared.models.post_model import Post
from notification_app.services.notification_service import NotificationService
from user_app.services.user_service import UserService 

class LikeService:
    def create_like(post_id,user_id,):
        like=Like(post_id,user_id)
        db.session.add(like)
        db.session.commit()
        try:
            post = Post.query.filter.get_post_by_id(post_id)
            NotificationService.create_notification(post.user_id,"Your post recieved a like from{UserService.get_user_by_id(user_id).username}")
        except:
            db.session.rollback()
        return like    

    def delete_like(like_id):
        like=Like.query.filter(like_id=like_id).first()
        db.session.delete(like)
        db.session.commit()
        return like
    

