from replit import db
import time
class Global_chat:
  @staticmethod
  def channels(channel_id):
    return db.prefix(f"{channel_id}")


