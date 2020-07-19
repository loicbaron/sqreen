import os
from datetime import date
from unittest.mock import patch, mock_open

from project.notifications.notify_log import NotifyLog

def test_constructor_without_root_path(tmp_path):
  notify = NotifyLog("logs")
  assert isinstance(notify, NotifyLog)

def test_get_path(tmp_path):
  path = NotifyLog("logs", str(tmp_path)).get_path("test_logs")
  assert "{}/test_logs".format(tmp_path) == path

def test_get_filename(tmp_path):
  today = date.today().strftime("%Y-%m-%d")
  filename = NotifyLog("logs", str(tmp_path)).get_filename()
  assert "{}/logs/{}.log".format(tmp_path, today) in filename

def test_write_to_file():
  open_mock = mock_open()
  with patch("project.notifications.notify_log.open", open_mock, create=True):
      notify = NotifyLog("logs")
      notify.write_to_file("test.txt", "message")
  open_mock.assert_called_with("test.txt", "a")
  open_mock.return_value.write.assert_called_once_with("message")

def test_send(tmp_path):
  notify = NotifyLog("logs", str(tmp_path))
  sent = notify.send("message")
  assert sent == True
  with open(notify.get_filename(), 'r') as f:
    assert f.read() == "message\n"

