from graphics import *
from event import *
from rect_checker import *

class App:
  def __init__(self):
    #the text objects for each button are here to easily draw and undraw them from main
    self.edit_text = None
    self.move_text = None
    self.delete_text = None
    self.load_text = None
    self.add_text = None

    #if an event repeats, holds where it repeats
    self.days_list = list()
    

  def times(self, p_time):
    #assigns a hour (0-24) to the point clicked on the calendar
    time = -1
    if p_time.x <= -82 and 82.2 < p_time.y < 90:
      time = 0
    elif p_time.x <= -82 and 74.6 < p_time.y < 82.2:
      time = 1
    elif p_time.x <= -82 and 67 < p_time.y < 74.6:
      time = 2
    elif p_time.x <= -82 and 59.4 < p_time.y < 67:
      time = 3
    elif p_time.x <= -82 and 51.8 < p_time.y < 59.4:
      time = 4
    elif p_time.x <= -82 and 44.2 < p_time.y < 51.8:
      time = 5
    elif p_time.x <= -82 and 36.6 < p_time.y < 44.2:
      time = 6
    elif p_time.x <= -82 and 29< p_time.y < 36.6:
      time = 7
    elif p_time.x <= -82 and 21.4 < p_time.y < 29:
      time = 8
    elif p_time.x <= -82 and 13.8 < p_time.y < 21.4:
      time = 9
    elif p_time.x <= -82 and 6.2 < p_time.y < 13.8:
      time = 10
    elif p_time.x <= -82 and -1.4 < p_time.y < 6.2:
      time = 11
    elif p_time.x <= -82 and -9 < p_time.y < -1.4:
      time = 12
    elif p_time.x <= -82 and -16.6 < p_time.y < -9:
      time = 13
    elif p_time.x <= -82 and -24.2 < p_time.y < -16.6:
      time = 14
    elif p_time.x <= -82 and -31.8 < p_time.y < -24.2:
      time = 15
    elif p_time.x <= -82 and -39.4 < p_time.y < -31.8:
      time = 16
    elif p_time.x <= -82 and -47 < p_time.y < -39.4:
      time = 17
    elif p_time.x <= -82 and -54.6 < p_time.y < -47:
      time = 18
    elif p_time.x <= -82 and -62.2 < p_time.y < -54.6:
      time = 19
    elif p_time.x <= -82 and -69.8 < p_time.y < -62.2:
      time = 20
    elif p_time.x <= -82 and -77.4 < p_time.y < -69.8:
      time = 21
    elif p_time.x <= -82 and -85 < p_time.y < -77.4:
      time = 22
    elif p_time.x <= -82 and -92.6 < p_time.y < -85:
      time = 23
    elif p_time.x <= -82 and -100 < p_time.y < -92.6:
      time = 24

    return time


  def day(self, p_day):
    #assigns a day number to the point clicked on the calendar
    if -100 <= p_day.x < -45.6:
      #monday
      day_date = 0
    elif -45.6 <= p_day.x < -8.6:
      #tuesday
      day_date = 1
    elif -8.6 <= p_day.x < 27.8:
      #wednesday
      day_date = 2
    elif 27.8 <= p_day.x < 64.2:
      #thursday
      day_date = 3
    elif 64.2 <= p_day.x < 100:
      #friday
      day_date = 4
    return day_date


  def isMultipleDays(self,win):
    #allows the user to print the same event over multiple days. for a repeating class or a practice schedule 

    #provides prompts to the user to add an event to multiple days
    ask_mult_day = Text(Point(0,10), "What days does it repeat?")
    ask_mult_day.setFace("helvetica")
    ask_mult_day_done = Text(Point(0, -10), "(click done button when complete)")
    ask_mult_day_done.setFace("helvetica")
    ask_mult_day_done.setStyle("italic")
    ask_mult_day.draw(win)
    ask_mult_day_done.draw(win)
    done_but = Rectangle(Point(100,-50), Point(82,-30))
    done_but.setFill("sky blue")
    done_text = Text(Point(91, -40), "Done")
    done_text.setFace("helvetica")
    done_text.setSize(8)
    done_but.draw(win)
    done_text.draw(win)

    #sets button that will become mouse clicker
    p_day2 = Point(-100,-100)

    #runs until the done button is pressed
    while not IsInRect(p_day2, done_but):
      p_day2 = win.getMouse()
      #creates a list of all of the days clicked
      new_day = self.day(p_day2)
      self.days_list.append(new_day)

    #undraws the instructions
    ask_mult_day.undraw()
    ask_mult_day_done.undraw()

    #since the done button is in friday, when it's clicked before ending the loop it adds a final friday object to the list. this removes that last extra item in the list  
    self.days_list.pop()

    #gets rid of the button    
    done_but.undraw()
    done_text.undraw()
    

  def menu(self,win): 
    #this menu takes the user through the process to add an event

    #provides propts to the user to add an event
    p1 = Point(-55,20)
    p2 = Point(55,-20)
    rect = Rectangle (p1,p2)
    rect.setFill('sky blue')
    rect.draw(win)
    #gets the day of the event from user
    get_date = Text(Point(0, 10), "What day is your event?")
    get_date.setFace("helvetica")
    get_date2 = Text(Point(0, -10), "(Click the day)")
    get_date2.setFace("helvetica")
    get_date2.setStyle("italic")
    get_date.draw(win)
    get_date2.draw(win)

    #when the user clicks on a day the program saves it
    p_day = win.getMouse()
    day_date = self.day(p_day)
    get_date.undraw()
    get_date2.undraw()

    #gets the start time of the event from user
    get_start = Text(Point(0, 10), "What time does your event start?")
    get_start.setFace("helvetica")
    get_start2 = Text(Point(0, -10), "(Click the time)")
    get_start2.setFace("helvetica")
    get_start2.setStyle("italic")
    get_start.draw(win)
    get_start2.draw(win)
    p_start_time = win.getMouse()
    start_time = self.times(p_start_time)
    get_start.undraw()
    get_start2.undraw()
    
    #gets the end time of the event from user
    get_end = Text(Point(0, 10), "What time does your event end?")
    get_end.setFace("helvetica")
    get_end2 = Text(Point(0, -10), "(Click the time)")
    get_end2.setFace("helvetica")
    get_end2.setStyle("italic")
    get_end.draw(win)
    get_end2.draw(win)
    p_end_time = win.getMouse()
    end_time = self.times(p_end_time)
    get_end.undraw()
    get_end2.undraw()
    
    #gets the title of the event from user
    get_title = Text(Point(0, 0), "What is the name of your event:")
    get_title.setFace("helvetica")
    get_title.draw(win)
    title = input("Enter title here:")
    get_title.undraw()


    #gets the category of event from user
    get_category = Text(Point(0, 0), "Is your event a school, work, or social event?")
    get_category.setFace("helvetica")
    get_category.draw(win)
    category = input('Enter the category:')
    get_category.undraw()

    #gets the answer as to whether theevent is repeating or not
    ask_multiple = Text(Point(0, 0), "Is your event a repeating event?")
    ask_multiple.setFace("helvetica")
    ask_multiple.draw(win)
    answer = input('Yes or no:')
    ask_multiple.undraw()
    if answer == 'yes':
      repeating = 'yes'
      #creates the multiple events
      self.isMultipleDays(win)
    elif answer == 'no':
      repeating = 'no'
    
    rect.undraw()

    #sends the event info to the event class
    event = Event(day_date, start_time, end_time, title, category)
    return event


  def menu_button(self,win):
    #this creates the menu button using graphics
    p1 = Point(-100, 100)
    p2 = Point(-82, 90)
    button = Rectangle(p1,p2)
    button.setFill("sky blue")
    button.draw(win)
    text = Text(Point(-91, 95), "Menu")
    text.setFace("helvetica")
    text.setSize(8)
    text.draw(win)
    return button


  def exit_button(self,win):
    #this creates the exit button which ends the program and saves all calendar data
    p1 = Point(100,-100)
    p2 = Point(82,-90)
    button = Rectangle(p1,p2)
    button.setFill("sky blue")
    button.draw(win)
    text = Text(Point(91,-95),"Exit")
    text.setFace("helvetica")
    text.setSize(8)
    text.draw(win)
    return button


  def load_event(self,win):
    #creates the load event button
    p1 = Point(-50, -40)
    p2 = Point(50, -60)
    load = Rectangle(p1, p2)
    load.setFill("sky blue")
    load.draw(win)
    self.load_text = Text(Point(0, -50), "Load Event")
    self.load_text.draw(win)
    return load


  def add_event(self,win):
    #creates the add event button
    p1 = Point (-50, 80)
    p2 = Point (50, 60)
    add_rect = Rectangle(p1,p2)
    add_rect.setFill('sky blue')
    add_rect.draw(win)
    self.add_text = Text(Point(0, 70), "Add Event")
    self.add_text.setFace("helvetica")
    self.add_text.draw(win)
    return add_rect

  def edit_event (self,win):
    #creates the edit event button
    p1 = Point(-50,50)
    p2 = Point(50,30)
    edit_rect = Rectangle(p1,p2)
    edit_rect.setFill("sky blue")
    edit_rect.draw(win)
    self.edit_text = Text(Point(0, 40), "Edit Title")
    self.edit_text.setFace("helvetica")
    self.edit_text.draw(win)
    return edit_rect


  def delete_event (self,win):
    #creates the delete event button
    p1 = Point(-50, 20)
    p2 = Point(50, 0)
    delete_rect = Rectangle(p1,p2)
    delete_rect.setFill("sky blue")
    delete_rect.draw(win)
    self.delete_text = Text(Point(0, 10), "Delete Event")
    self.delete_text.setFace("helvetica")
    self.delete_text.draw(win)
    return delete_rect

  def move_event (self,win):
    #creates the move event button
    p1 = Point(-50, -10)
    p2 = Point(50, -30)
    move_rect = Rectangle(p1,p2)
    move_rect.setFill("sky blue")
    move_rect.draw(win)  
    self.move_text = Text(Point(0, -20), "Move Event")
    self.move_text.setFace("helvetica")
    self.move_text.draw(win)
    return move_rect

