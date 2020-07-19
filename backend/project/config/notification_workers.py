import os
from project.notifications.notify_email import NotifyEmail
from project.notifications.notify_log import NotifyLog

root_path = os.path.join(os.path.dirname(__file__), '../..')

smtp_server = os.environ.get('EMAIL_SMTP_HOST')
port = int(os.environ.get("EMAIL_SMTP_TLS_PORT") or 587)  # For starttls
password = os.environ.get('EMAIL_PASSWORD')
sender_email = os.environ.get('EMAIL_SENDER')
receiver_email = os.environ.get('EMAIL_RECEIVER')

workers = [
  NotifyLog("logs", root_path),
  NotifyEmail("email", smtp_server, port, sender_email, password, receiver_email)
]