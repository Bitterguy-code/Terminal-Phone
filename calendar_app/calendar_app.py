from user import User
import calendar
import cowsay


##ADD DELETE USER
##ADD DELETE/ARCHIVE EVENTS

class Calendar:

  users = {}

  ##No particular order
  archive = []

  def __init__(self):
    pass

  ##Option 1
  @classmethod
  def create_a_user(cls):
    print("Creating a new user for calendar...")
    name_input = input("What is the user's name?: ").lower()
    while name_input in cls.users and name_input != 'q':
      print(f"'{name_input}' already exists. Try a different name")
      name_input = input("What is the user's name?: ").lower()
    if name_input == 'q':
      return 'q'
    cls.users[name_input] = User(name_input)
    return(f"{name_input} has been successfully added as a user.")
  

  ##Option 2
  @classmethod
  def display_all_users(cls):
    if not cls.users:
      return 'q'
    else:
      for index, user in enumerate(cls.users):
        print(f"{index+1}. {user}")


  ##Option 3
  @classmethod
  def create_event(cls):
    print("Who would you like to create an event for?")
    found_user = input("Input name: ")
    found_user = cls.select_a_user(found_user)
    if found_user == 'q':
      return 'q'
    if found_user:
      event_title = input("Event title/name: ")

      event_date = input("Event date(YYYYMMDD): ")
      while len(event_date) > 8 or len(event_date) <= 7:
        print("Incorrect date format. Please try again")
        event_date = input("Event date(YYYYMMDD): ")
      
      try:
        event_time = int(input("Event time(0000-2400): "))
        while event_time > 2400 or event_time < 0:
          print("You need to input a time between 0000-2400")
          event_time = int(input("Event time(0000-2400): "))
      except ValueError:
        print("You need to input an int for time")
        print("Quitting cause I hate python")
        return 'q'
      
      found_user.events[event_title] = {
        "event_owner": found_user.name,
        "event_title": event_title,
        "event_date": event_date,
        "event_time": event_time
      }
      return(f"{event_title} has been successfully added for {found_user.name}")
      
    else:
      return 'User not found. Quitting event creation...'


  ##Option 4
  @classmethod
  def display_user_events(cls):
    print("Which user's events do you wish to see?")
    found_user = input("Input name: ")
    found_user = cls.select_a_user(found_user)
    if found_user == 'q':
      return 'q'
    if found_user:
      if len(found_user.events) < 1:
        return(f"{found_user.name} has no events currently...")
      print(found_user.events)
      print(f"{found_user.name} has these events:")
      for event in found_user.events.values():
        print(
f"""
____________

{event["event_date"]} - {event["event_time"]}

  -  {event["event_title"]}

____________
""")
    else:
      return('User not found. Quitting user event display...')

  ##Option 5
  @classmethod
  def delete_user(cls):
    print("Which user would you like to delete?")
    found_user = input("Input name: ")
    if found_user == 'q' or not cls.select_a_user(found_user):
      return 'q'
    else:
      found_user = cls.select_a_user(found_user)
      cls.users.pop(found_user.name)


  ##Option 6
  @classmethod
  def archive_event(cls):
    print("Which user would you like to select for an event archival?")
    found_user = input("Input name: ")
    if found_user == "q" or not cls.select_a_user(found_user):
      print(f"User: '{found_user}' not found.")
      return 'q'
    else:
      temp_arr = []
      found_user = cls.select_a_user(found_user)
      for index, event in enumerate(found_user.events):
        temp_arr.append(event)
        print(f"{index + 1}. {event}")
      if len(temp_arr) <= 0:
        return "User has no events to archive."
      event_input = None
      while True:
        try:
          print("Choose one of the following events(input '1337' to quit)")
          event_input = int(input("Event index: "))
          if event_input == 1337:
            return "q"
          break
        except ValueError:
          print("You need to input an int...")
      if event_input == None or not found_user.events[event]:
        print("There is no event that matches that index")
      else:
        if event_input > len(temp_arr):
          print("Index out of range.")
          return "q"
        removed_event = temp_arr.pop(event_input-1)
        cls.archive.append([found_user.name, removed_event])
        del found_user.events[removed_event]
        return f"{removed_event} has been archived."


  @classmethod
  def see_all_archived_events(cls):
    for event in cls.archive:
      print(event)

  ##Option 8
  @classmethod
  def year(cls):
    try:
      year_int = int(input("What year do you want to take a peek at?: "))
      if year_int == 1337:
        return 'q'
      else:
        print(calendar.calendar(year_int))
    except ValueError:
      print("You need to input an integer")
      cls.year()

  ##Option 9
  @classmethod
  def month(cls):
    try:
      print("Which month(1-12) and year do you want to peek at?")
      year_input = int(input("Year: "))
      if year_input == 1337:
        return 'q'
      month_input = int(input("Month: "))
      if year_input == 1337:
        return 'q'
      else:
        print(calendar.month(year_input, month_input))
    except ValueError:
      print("You need to input integers for both")
      cls.month()


  ##Support function
  @classmethod
  def select_a_user(cls, name_to_find):
    return cls.users.get(name_to_find) ##Returns User object


  ##Runner
  @classmethod
  def run_calendar(cls):
    print(
r"""
   _____          _      ______ _   _ _____          _____  
  / ____|   /\   | |    |  ____| \ | |  __ \   /\   |  __ \ 
 | |       /  \  | |    | |__  |  \| | |  | | /  \  | |__) |
 | |      / /\ \ | |    |  __| | . ` | |  | |/ /\ \ |  _  / 
 | |____ / ____ \| |____| |____| |\  | |__| / ____ \| | \ \ 
  \_____/_/    \_\______|______|_| \_|_____/_/    \_\_|  \_\
                                                            
                (type "q" to exit the program)  
  
    1. Create a user
    2. Display all users
    3. Create an event for a user
    4. Display all events for a specific user
    5. Delete a user
    6. Archive(Delete) an event
    7. See all archived events
    8. See yearly calendar
    9. See monthly calendar

""")
    user_decision = input("Choose one of the above options(number): ")

    match user_decision:
      case "1":
        returner = cls.create_a_user()
        if returner == 'q':
          print("Exiting option 1\n")
          cls.run_calendar()
        else:
          print(returner, "\n")
          cls.run_calendar()
      case "2":
        returner = cls.display_all_users()
        if returner == "q":
          print(f"No users created yet\n")
          cls.run_calendar()
        else:
          cls.run_calendar()
      case "3":
        returner = cls.create_event()
        if returner == "q":
          print("Exiting option 3\n")
          cls.run_calendar()
        else:
          print(returner, "\n")
          cls.run_calendar()
      case "4":
        returner = cls.display_user_events()
        if returner == "q":
          print("Exiting option 4\n")
          cls.run_calendar()
        else:
          print(returner, "\n")
          cls.run_calendar()
      case "5":
        returner = cls.delete_user()
        if returner == "q":
          print("Exiting option 5\n")
          cls.run_calendar()
        else:
          cls.run_calendar()
      case "6":
        returner = cls.archive_event()
        if returner == "q":
          print("Exiting option 6\n")
          cls.run_calendar()
        else:
          print(returner)
          cls.run_calendar()
      case "7":
        returner = cls.see_all_archived_events()
        if returner == "q":
          print("Exiting option 7\n")
          cls.run_calendar()
        else:
          cls.run_calendar()
      case "8":
        returner = cls.year()
        if returner == "q":
          print("Exiting option 7\n")
          cls.run_calendar()
        else:
          cls.run_calendar()
      case "9":
        returner = cls.month()
        if returner == "q":
          print("Exiting option 8\n")
          cls.run_calendar()
        else:
          cls.run_calendar()
      case 'q':
        cowsay.cow("Goodbye! See you next time!(Your data has been uploaded to the chinese servers and has been wiped)")
      case _:
        print(f"Try another value")
        cls.run_calendar()

# print(Calendar.archive)
# google = Calendar()
# google.run_calendar()
# google.year()
# google.month()
# google.create_a_user() 
# google.create_a_user()

# google.display_all_users()


# print(google.create_event())
# print(google.create_event())
# print(google.create_event())

# print(google.display_user_events())

