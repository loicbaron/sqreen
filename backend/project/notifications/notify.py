from abc import ABCMeta, abstractmethod
"""
Formal interface
  using Abstract Method Declaration
"""

class NotifyInterface(metaclass=ABCMeta):
  
  @abstractmethod
  def __init__(self, name: str):
    self.name = name
  
  @abstractmethod
  def send(self, message: str) -> bool:
    raise NotImplementedError

