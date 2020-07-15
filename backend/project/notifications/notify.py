"""
informal interface
  duck typing to inform users that this is an interface
  and should be used accordingly
"""
# todo: use abc.ABCMeta Formal interface

class NotifyInterface:

  def __init__(self, message):
    self.message = message

  def send(self) -> bool:
    pass

