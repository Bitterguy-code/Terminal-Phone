import datetime
import calendar

class User:

  def __init__(self, name):
    self.name = name
    self.events = {}
    # 'event_title': {
    #   "event_owner": "Chungus",
    #   "event_title": "birthday",
    #   "event_date": '2025 12 31',
    #   "event_time": "1300",
    # }

  
  
  # def __repr__(self):
  #   return f"{self.name} has these events: {self.events}\n"
  