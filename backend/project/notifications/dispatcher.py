import os
from project.notifications.notify_email import NotifyEmail
from project.notifications.notify_log import NotifyLog

"""
This service could be independant from the Flask app
Could be further developed as a dedicated micro service
"""

def dispatch(message: str) -> dict:
  result = {}
  # todo: 
  #   import and instanciate Dynamically based on env vars
  #   try except and continue to handle errors on one of the targets
  #   results could be stored in DB
  try:
    root_path = os.path.join(os.path.dirname(__file__), '../..')
    log_written = NotifyLog(message, root_path).send()
    result['log'] = log_written

    smtp_server = os.environ.get('EMAIL_SMTP_HOST')
    port = int(os.environ.get("EMAIL_SMTP_TLS_PORT") or 587)  # For starttls
    password = os.environ.get('EMAIL_PASSWORD')
    sender_email = os.environ.get('EMAIL_SENDER')
    receiver_email = os.environ.get('EMAIL_RECEIVER')
    email_sent = NotifyEmail(message, smtp_server, port, sender_email, password, receiver_email).send()
    result['email'] = email_sent
  except Exception:
    import traceback
    traceback.print_exc()
  return result