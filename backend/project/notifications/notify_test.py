from project.notifications.notify import NotifyInterface

class NotifyTest(NotifyInterface):

  def __init__(self, name: str):
    super().__init__(name)

  def send(self, message: str) -> bool:
    print("NotifyTest send => {}".format(message))
    return True


class NotifyTestException(NotifyInterface):

  def __init__(self, name: str):
    super().__init__(name)

  def send(self, message: str) -> bool:
    print("NotifyTestException send => {}".format(message))
    raise Exception("NotifyTestException")

