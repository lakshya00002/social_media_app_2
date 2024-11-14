from flask import Blueprint,request
from like_app.controllers.like_controller import LikeController

like_bp=Blueprint('like_bp',__name__)

@like_bp.route('/likes',methods=['POST'])
def create_like(user_id,post_id):
    data=request.json
    user_id=data.get('user_id')
    post_id=data.get('post_id')
    if not user_id or not post_id:
        return {"error":"Missing requuired data"}
    return LikeController.create_like(user_id,post_id)

@like_bp.route('/likes/<like_id>',methods=['DELETE'])
def delete_like(like_id):
    return LikeController.delete_like(like_id)


