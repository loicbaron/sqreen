from unittest.mock import patch

from project.notifications.dispatcher import dispatch
from project.notifications.notify_test import NotifyTest, NotifyTestException

def test_dispatch():
  workers = [ NotifyTest("test1"), NotifyTest("test2") ]
  result = dispatch("message", workers)
  assert len(result) == 2
  assert result['test1'] == True
  assert result['test2'] == True

def test_dispatch_with_exception():
  workers = [ NotifyTestException("test1"), NotifyTest("test2") ]
  result = dispatch("message", workers)
  assert len(result) == 1
  assert result['test2'] == True

