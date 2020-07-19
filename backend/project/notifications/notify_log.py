import os
from datetime import date

from project.notifications.notify import NotifyInterface

class NotifyLog(NotifyInterface):

  def __init__(self, name: str, root_path: str = None):
    if root_path:
      self.root_path = root_path
    else:
      self.root_path = os.path.join(os.path.dirname(__file__), '../..')
    super().__init__(name)

  def get_path(self, folder_name: str) -> str:
    logs_folder = "{}/{}".format(self.root_path, folder_name)
    if not os.path.exists(logs_folder):
      os.makedirs(logs_folder)
    return logs_folder

  def get_filename(self) -> str:
    # todo: parse message to get more relevant log file (ex: per app monitored, type of event)
    path = self.get_path("logs")
    today = date.today().strftime("%Y-%m-%d")
    return "{}/{}.log".format(path, today)

  def send(self, message) -> bool:
    try:
      filename = self.get_filename()
      self.write_to_file(filename, message)
      self.write_to_file(filename, "\n")
    except Exception:
      import traceback
      traceback.print_exc()
      return False
    return True

  def write_to_file(self, filename: str, line: str):
    with open(filename, 'a') as f:
      f.write(line)

