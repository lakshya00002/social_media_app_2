from shared.models.post_model import Post
from shared.utils.db_utils import db
from user_app.services.user_service import UserService
from notification_app.services.notification_service import NotificationService
from shared.models.user_model import User

class PostService:
    @staticmethod
    def create_post(user_id, content):
        new_post = Post(user_id=user_id, content=content)
        db.session.add(new_post)
        db.session.commit()
        try:
          NotificationService.create_notification(user_id,f"Your post has been successfully created.")

          followers=UserService.get_all_users()
          for follower in followers:
            NotificationService.create_notification(follower.user_id,f"user {User.username} created a new post")
        except:
            db.session.rollback()
            print('Error creating post')

        return new_post
    


    @staticmethod
    def get_post_by_id(post_id):
        return Post.query.filter_by(post_id=post_id).first()

    @staticmethod
    def get_posts_by_user(user_id):
        return Post.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_all_posts():
        return Post.query.order_by(Post.created_at.desc()).all()

    @staticmethod
    def update_post(post_id, new_content):
        post = Post.query.filter_by(post_id=post_id).first()
        if post:
            post.content = new_content
            db.session.commit()

        NotificationService.create_notification(post.user_id,f"Your post with post_id{post.post_id} has been succesfully updated.")

        return post

    @staticmethod
    def delete_post(post_id):
        post = Post.query.filter_by(post_id=post_id).first()
        if post:
            db.session.delete(post)
            db.session.commit()

        NotificationService.create_notification(post.user_id,f"Your post with post_id{post.post_id} has been successfully updated.")

        return post
    
  
