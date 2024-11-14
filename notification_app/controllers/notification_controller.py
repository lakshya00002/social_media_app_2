from notification_app.services.notification_service import NotificationService

class NotificationController:
    @staticmethod
    def get_user_notifications(user_id):
        notifications= NotificationService.get_notification(user_id)
        return [notification.message for notification in notifications]

    
    @staticmethod
    def send_notification(user_id,message):
        return NotificationService.create_notification(user_id,message)
    
    @staticmethod
    def mark_as_read(notification_id):
        return NotificationService.mark_as_read(notification_id)