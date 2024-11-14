from flask import Blueprint, jsonify
from notification_app.controllers.notification_controller import NotificationController

notification_bp= Blueprint('notification_bp', __name__)

@notification_bp.route('/api/users/<int:user_id>/notifications',methods=['GET'])
def get_notifications(user_id):
    notifications=NotificationController.get_user_notifications(user_id)
    return jsonify({"notifications":notifications}),200

@notification_bp.route('/api/notifications/<int:notification_id>/notifications',methods=['POST'])
def mark_notification_as_read(notification_id):
    NotificationController.mark_as_read(notification_id)
    return jsonify({'message':"Notification mark as read"}),200