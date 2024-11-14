from flask import Blueprint,request
from comment_app.controllers.comment_controller import CommentController

comment_bp =Blueprint('comment_bp',__name__)

@comment_bp.route('/comments',methods=['POST'])
def create_comment(user_id,post_id,content):
    data=request.json
    user_id=data.get('user_id')
    post_id=data.get('post_id')
    content=data.get('content')

    if not user_id or not post_id or not content:
        return {"error":"Missing required data"}

    return CommentController.create_comment(user_id,post_id,content)


@comment_bp.route('/comments/<comment_id>',methods=['POST'])
def update_comment(comment_id,content):
    return CommentController.create_comment(comment_id,content)

@comment_bp.route('/comments/<comment_id>',methods=['POST'])
def delete_comment(comment_id):
    return CommentController.delete_comment(comment_id)
