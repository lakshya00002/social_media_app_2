from flask import Blueprint, request
from follow_app.controller.follow_controller import FollowController

follow_bp=Blueprint('follow_bp',__name__)

@follow_bp.route('/follow',methods=['POST'])
def follow(follower_username,followee_username):
    data=request.get_json()
    follower_username=data.get('follower_username')
    followee_username=data.get('followee_username')
    return FollowController.follow(follower_username,followee_username)

@follow_bp.route('/unfollow',methods=['DELETE'])
def unfollow(follower_username,followee_username):
    data=request.get_json()
    follower_username=data.get('follower_username')
    followee_username=data.get('follwer_username')
    return FollowController.unfollow(follower_username,followee_username)
