import os
from typing import List

from project.notifications.notify import NotifyInterface

"""
This service could be independant from the Flask app
Could be further developed as a dedicated micro service
"""

def dispatch(message: str, workers: List[NotifyInterface]) -> dict:
  result = {}
  for worker in workers:
    try:
      result[worker.name] = worker.send(message)
    except Exception:
      import traceback
      traceback.print_exc()
      continue
  return result