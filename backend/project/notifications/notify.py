from abc import ABCMeta, abstractmethod
"""
Formal interface
  using Abstract Method Declaration
"""

class NotifyInterface(metaclass=ABCMeta):
  
  @abstractmethod
  def __init__(self, message):
    self.message = message
  
  @abstractmethod
  def send(self) -> bool:
    raise NotImplementedError

