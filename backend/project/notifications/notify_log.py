import os
from datetime import date
from project.notifications.notify import NotifyInterface

class NotifyLog(NotifyInterface):

  def get_file_name(self) -> str:
    # todo: parse self.message to get more relevant log file (ex: per app monitored, type of event)
    APP_ROOT = os.path.join(os.path.dirname(__file__), '../..')
    logs_folder = "{}/logs".format(APP_ROOT)
    if not os.path.exists(logs_folder):
      os.makedirs(logs_folder)
    today = date.today().strftime("%Y-%m-%d")
    return "{}/logs/{}.log".format(APP_ROOT, today)

  def send(self) -> bool:
    try:
      with open(self.get_file_name(), 'a') as f:
        f.write(self.message)
        f.write("\n")
    except Exception:
      import traceback
      traceback.print_exc()
      return False
    return True
