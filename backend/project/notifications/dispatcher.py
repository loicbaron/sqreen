from project.notifications.notify_email import NotifyEmail
from project.notifications.notify_log import NotifyLog

"""
This service could be independant from the Flask app
Could be further developed as a dedicated micro service
"""

def dispatch(message: str) -> list:
  results = []
  # todo: 
  #   import and instanciate Dynamically based on env vars
  #   try except and continue to handle errors on one of the targets
  #   results could be stored in DB
  try:
    log_written = NotifyLog(message).send()
    results.append({'log': log_written})

    email_sent = NotifyEmail(message).send()
    results.append({'email': email_sent})
  except Exception:
    import traceback
    traceback.print_exc()
  return results