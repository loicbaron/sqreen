import pytest
from unittest.mock import patch

from project.notifications.notify_email import NotifyEmail

smtp_server = ""
port = 587
password = ""
sender_email = ""
receiver_email = ""

def my_side_effect():
    raise Exception("Test")

def test_get_subject():
  notify = NotifyEmail("message", smtp_server, port, sender_email, password, receiver_email)
  assert notify.get_subject() == "Notification from Sqreen"

def test_get_connection():
  notify = NotifyEmail("message", smtp_server, port, sender_email, password, receiver_email)
  with patch("smtplib.SMTP") as mock_smtp:
    notify.get_connection()
    instance = mock_smtp.return_value
    assert instance.ehlo.call_count == 2
    assert instance.starttls.called == True
    assert instance.login.called == True

def test_send():
  notify = NotifyEmail("message", smtp_server, port, sender_email, password, receiver_email)
  with patch("smtplib.SMTP") as mock_smtp:
    notify.send()
    instance = mock_smtp.return_value
    assert instance.sendmail.called == True
    instance.sendmail.assert_called_once_with(
      sender_email, 
      receiver_email, 
      'Subject: {}\n\n{}'.format(notify.get_subject(), notify.message)
    )
