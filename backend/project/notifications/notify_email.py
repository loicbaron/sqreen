import os
import smtplib, ssl

from project.notifications.notify import NotifyInterface

class NotifyEmail(NotifyInterface):

  def __init__(self, name: str, smtp_server: str, port: int, sender_email: str, password: str, receiver_email: str):
    self.smtp_server = smtp_server
    self.port = port
    self.sender_email = sender_email
    self.password = password
    self.receiver_email = receiver_email
    super().__init__(name)

  def get_subject(self) -> str:
    # todo: parse message to get more relevant Subject (ex: per app monitored, type of event)
    return "Notification from Sqreen"

  def get_connection(self) -> smtplib.SMTP:
    # Create a secure SSL context
    context = ssl.create_default_context()
    # Try to log in to server and send email
    server = smtplib.SMTP(self.smtp_server, self.port)
    server.ehlo()
    server.starttls(context=context) # Secure the connection
    server.ehlo()
    server.login(self.sender_email, self.password)
    return server

  def send(self, message) -> bool:
    result = False
    try:
        # smtp connection
        server = self.get_connection()
        # send email
        server.sendmail(self.sender_email, self.receiver_email, 'Subject: {}\n\n{}'.format(self.get_subject(), message))
        result = True
        server.quit()
    except Exception as e:
        import traceback
        traceback.print_exc()
    finally:
        return result
