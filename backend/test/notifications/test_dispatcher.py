from unittest.mock import patch

from project.notifications.dispatcher import dispatch

def test_dispatch():
  with patch("project.notifications.notify_log.NotifyLog.send") as mock_notify_log, patch("project.notifications.notify_email.NotifyEmail.send") as mock_notify_email:
    mock_notify_log.return_value = True
    mock_notify_email.return_value = True
    result = dispatch("message")
    assert len(result) == 2
    assert result['log'] == True
    assert result['email'] == True
