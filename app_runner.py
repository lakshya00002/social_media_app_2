import subprocess

# Run the service corresponding to the user_app
def run_user_service():
    subprocess.Popen(["/Users/lakshya./Downloads/version_2/social_media_app/venv/bin/python", "user_app/app.py"])


# Run the service corresponding to the post_app
def run_post_service():
    subprocess.Popen(["/Users/lakshya./Downloads/version_2/social_media_app/venv/bin/python", "post_app/app.py"])

# Run the service corresponding to the comment_app
def run_comment_service():
    subprocess.Popen(["/Users/lakshya./Downloads/version_2/social_media_app/venv/bin/python","comment_app/app.py"])

# Run the service corresponding to the like_app
def run_like_service():
    subprocess.Popen(["/Users/lakshya./Downloads/version_2/social_media_app/venv/bin/python","like_app/app.py"]) 

# Run the service corresponding to the message_app
def run_message_service():
    subprocess.Popen(["/Users/lakshya./Downloads/version_2/social_media_app/venv/bin/python","message_app/app.py"])           

# Run the service corresponding to the notification_app
def run_notification_service():
    subprocess.Popen(["/Users/lakshya./Downloads/version_2/social_media_app/venv/bin/python","notification_app/app.py"])

# Run the service corresponding to the follow_app
def run_follow_service():
    subprocess.Popen(["/Users/lakshya./Downloads/version_2/social_media_app/venv/bin/python","follow_app/app.py"])

if __name__ == '__main__':
    run_user_service()
    run_post_service()
    run_comment_service()
    run_like_service()
    run_message_service()
    run_notification_service()
    run_follow_service()

    # Graceful Termination of the two subprocesses
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nTerminating both the processes. Alvida!")
