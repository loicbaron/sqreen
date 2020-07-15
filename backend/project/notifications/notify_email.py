import os
import smtplib, ssl

from project.notifications.notify import NotifyInterface

class NotifyEmail(NotifyInterface):

  def get_subject(self) -> str:
    # todo: parse self.message to get more relevant Subject (ex: per app monitored, type of event)
    return "Notification from Sqreen"

  def send(self) -> bool:
    smtp_server = os.environ.get('EMAIL_SMTP_HOST')
    port = int(os.environ.get("EMAIL_SMTP_TLS_PORT") or 587)  # For starttls
    sender_email = os.environ.get('EMAIL_SENDER')
    password = os.environ.get('EMAIL_PASSWORD')
    receiver_email = os.environ.get('EMAIL_RECEIVER')
    result = False
    try:
        # Create a secure SSL context
        context = ssl.create_default_context()
        # Try to log in to server and send email
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()
        server.starttls(context=context) # Secure the connection
        server.ehlo()
        server.login(sender_email, password)
        # send email
        server.sendmail(sender_email, receiver_email, 'Subject: {}\n\n{}'.format(self.get_subject(), self.message))
        result = True
    except Exception as e:
        import traceback
        traceback.print_exc()
    finally:
        server.quit()
        return result
