from shared.utils.db_utils import db
from notification_app.services.notification_service import NotificationService
from shared.models.follow_model import Follow
from user_app.services.user_service import UserService

class FollowService:
    @staticmethod
    def follow(follower_username,followee_username):
        follow=Follow(follower_username,followee_username)
        db.session.add(follow)
        db.session.commit()

        try:
            
            NotificationService.create_notification(followee_username,"{UserService.get_user_by_username(username) started to follow you}")
        except:
            db.session.rollback()
        
    
        return follow
    
    @staticmethod
    def unfollow(follower_username,followee_username):
        follow = Follow.query.filter_by(follower_username=follower_username,followee_username=followee_username)
        if follow:
            db.session.delete(follow)
            db.session.commit()

        return follow    


        


