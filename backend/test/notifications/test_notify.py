import pytest
from project.notifications.notify import NotifyInterface

def test_notify_interface_constructor():
  with pytest.raises(TypeError) as excinfo:
    NotifyInterface("message")
