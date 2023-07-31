from graphics import *
import base_calendar
from event import *
from app import *
from week import *
from day import *
from rect_checker import*

monday = Day("Monday*")
tuesday = Day("Tuesday*")
wednesday = Day("Wednesday*")
thursday = Day("Thursday*")
friday = Day("Friday*")

#days of the week list
week = Week(monday,tuesday,wednesday,thursday,friday)
#list of lists. inner list: each day's events in txt form. outer list: all of the days
week_txt = [monday.events_txt, tuesday.events_txt, wednesday.events_txt, thursday.events_txt, friday.events_txt]


def main():
  #Create a white window for weekly calendar
  win = GraphWin('Academic Schedule', 550, 550)
  win.setBackground('white')
  win.setCoords(-100,-100,100,100)
  base_calendar.make_base_calendar(win)
  #build the template calendar from the base_calendar file

  #creates app instance then draws menu and exit buttons
  app = App()
  menu_button = app.menu_button(win)
  exit_button = app.exit_button(win)

  #sets the variable that will later hold where the user clicks
  point_button = Point(-100,-100)
  #loop allows the user to add events and interact with the calendar until the exit button is pressed
  while not IsInRect(point_button, exit_button):

    point_button = win.getMouse()
     
    #if the add button is pressed, then the menu pops up
    if IsInRect(point_button, menu_button):
      #draws the 5 buttons that make up the menu and saves the rectangles for later
      add = app.add_event(win)
      edit = app.edit_event(win)
      delete = app.delete_event(win)
      move = app.move_event(win)
      load = app.load_event(win)     

       #resets the mouse clicker
      mouse_click = win.getMouse()


      #if the load button is pressed
      if IsInRect(mouse_click, load):
        #undraws all of the buttons 
        load.undraw()
        app.load_text.undraw()
        add.undraw()
        app.add_text.undraw()
        edit.undraw()
        app.edit_text.undraw()
        delete.undraw()
        app.delete_text.undraw()
        move.undraw()
        app.move_text.undraw()

        f = open("saved_cal.txt", "r")
        #opens calendar file for reading

        content = f.read()
        #splits into a list of the days
        num_lines = content.split("\n")

        #iterates through each line (which is a day of the week)
        for i in range(len(num_lines)):
          day_events = num_lines[i]

          #gets day string
          for j in range(len(day_events)):
            if day_events[j] == "*":
              day = "None"
              day = day_events[0:j]
              ast = -1
              ast = j+1
              #print(day)
              day_date = daystr_to_num(day)
              break

          #holds a string of all of the events in a day
          events_in_day = day_events[ast:]
          #turns that string into a list, separating by commas
          event_list = events_in_day.split(',')
          #since each item ends in a comma, removes the last extra item
          event_list.pop()
          
          #breaks up each event in event_list into all of the pieces that make up an event (separated by "-")
          for k in event_list:
            new_event = k.split('-')
            start_time = int(new_event[0])
            end_time = int(new_event[1])
            title = str(new_event[2])
            category = str(new_event[3])

            #creates the event
            new_event = Event(day_date, start_time, end_time, title, category)
            #draws the event
            new_event.make_event(win)
            #adds it to the list
            event_to_day(new_event)
             
      #if add button is clicked
      if IsInRect(mouse_click, add):
        #undraws the menu
        load.undraw()
        app.load_text.undraw()
        add.undraw()
        app.add_text.undraw()
        edit.undraw()
        app.edit_text.undraw()
        delete.undraw()
        app.delete_text.undraw()
        move.undraw()
        app.move_text.undraw()

        #calls app.menu to walk the user through building an event, then saves it
        event1 = app.menu(win)
        #copy for possible multiple events
        event1_copy = event1
        #draws the event
        event1.make_event(win)
        #creates the txt to represent event when the program is saved
        e_txt = event1.event_txt()

        #if the user adds multiple days, then the dayCopies method is called
        if len(app.days_list) >=1:
          dayCopies(win, event1_copy, app.days_list)
        #clears the list so it can be used again
        app.days_list = []
        #sends the event to the list of events for that day
        event_to_day(event1)
        
      #if edit button is picked
      if IsInRect(mouse_click, edit):
        #removes the menu
        load.undraw()
        app.load_text.undraw()
        add.undraw()
        app.add_text.undraw()
        edit.undraw()
        app.edit_text.undraw()
        delete.undraw()
        app.delete_text.undraw()
        move.undraw()
        app.move_text.undraw()

        #clears the mouse getter variable
        mouse_click = win.getMouse()

        #changes an event title for an event on monday 
        if app.day(mouse_click) == 0:
          for i in monday.events:
            if IsInRect(mouse_click, i.rect): 
              i.title = input("Enter a new title: ")
              new = Event(i.day_date, i.start_time, i.end_time, i.title, i.category)
              new.make_event(win)
              event_to_day(new)
              i.rect.undraw()
              break
              
        #changes an event title for an event on tuesday 
        elif app.day(mouse_click) == 1:
          for i in tuesday.events:
            if IsInRect(mouse_click, i.rect):
              i.title = input("Enter a new title: ")
              new = Event(i.day_date, i.start_time, i.end_time, i.title, i.category)
              new.make_event(win)
              event_to_day(new)
              i.rect.undraw()
              break

        #changes an event title for an event on wednesday 
        elif app.day(mouse_click) == 2:
          for i in wednesday.events:
            if IsInRect(mouse_click, i.rect):
              i.title = input("Enter a new title: ")
              new = Event(i.day_date, i.start_time, i.end_time, i.title, i.category)
              new.make_event(win)
              event_to_day(new)
              i.rect.undraw()
              break

        #changes an event title for an event on thursday 
        elif app.day(mouse_click) == 3:
          for i in thursday.events:
            if IsInRect(mouse_click, i.rect):
              i.title = input("Enter a new title: ")
              new = Event(i.day_date, i.start_time, i.end_time, i.title, i.category)
              new.make_event(win)
              event_to_day(new)
              i.rect.undraw()
              break

        #changes an event title for an event on friday 
        elif app.day(mouse_click) == 4:
          for i in friday.events:
            if IsInRect(mouse_click, i.rect):
             i.title = input("Enter a new title: ")
             new = Event(i.day_date, i.start_time, i.end_time, i.title, i.category)
             new.make_event(win)
             event_to_day(new)
             i.rect.undraw()
             break
   

      #if delete box is clicked
      elif IsInRect(mouse_click, delete):
        #undraws the menu box
        load.undraw()
        app.load_text.undraw()
        add.undraw()
        app.add_text.undraw()
        edit.undraw()
        app.edit_text.undraw()
        delete.undraw()
        app.delete_text.undraw()
        move.undraw()
        app.move_text.undraw()

        #clears mouse getter
        mouse_click = win.getMouse()

        #deletes an event in monday
        if app.day(mouse_click) == 0:
          for i in monday.events:
            if IsInRect(mouse_click, i.rect): 
              #undraws the rectangle
              i.rect.undraw()
              #deletes the event from the list
              i.delete_event(win)
              del i

        #deletes an event in tuesday
        elif app.day(mouse_click) == 1:
          for i in tuesday.events:
            if IsInRect(mouse_click, i.rect):
              i.delete_event(win)
              i.rect.undraw()
              del i

        #deletes an event in wednesday
        elif app.day(mouse_click) == 2:
          for i in wednesday.events:
            if IsInRect(mouse_click, i.rect):
              i.delete_event(win)
              i.rect.undraw()
              del i

        #deletes an event in thursday
        elif app.day(mouse_click) == 3:
          for i in thursday.events:
            if IsInRect(mouse_click, i.rect):
              i.delete_event(win)
              i.rect.undraw()
              del i

         #deletes an event in friday
        elif app.day(mouse_click) == 4:
          for i in friday.events:
            if IsInRect(mouse_click, i.rect):
              i.delete_event(win)
              i.rect.undraw()
              del i
        
      #if move button is clicked
      elif IsInRect(mouse_click, move):
        #removes menu
        add.undraw()
        app.add_text.undraw()
        edit.undraw()
        app.edit_text.undraw()
        delete.undraw()
        app.delete_text.undraw()
        move.undraw()
        app.move_text.undraw()
        load.undraw()
        app.load_text.undraw()

        #gives instructions to the user about how to move events
        p1 = Point(-55,20)
        p2 = Point(55,-20)
        move_rect = Rectangle (p1,p2)
        move_rect.setFill('sky blue')
        move_rect.draw(win)  
        move_txt = Text(Point(0, 0), "What event would you like to move?")
        move_txt.setFace("helvetica")
        move_txt.draw(win)

        move_click = win.getMouse()
        #moves event to monday
        if app.day(move_click) == 0:
          for i in monday.events:
            if IsInRect(move_click, i.rect):
              move_day(win, i)
              #undraws move instructions
              move_rect.undraw()
              move_txt.undraw()

        #moves event to tuesday
        elif app.day(move_click) == 1:
          for i in tuesday.events:
            if IsInRect(move_click, i.rect):
              move_day(win, i)
              move_rect.undraw()
              move_txt.undraw()

        #moves event to wednesday
        elif app.day(move_click) == 2:
          for i in wednesday.events:
            if IsInRect(move_click, i.rect):
              move_day(win, i)
              move_rect.undraw()
              move_txt.undraw()

        #moves event to thursday
        elif app.day(move_click) == 3:
          for i in thursday.events:
            if IsInRect(move_click, i.rect):
              move_day(win, i)
              move_rect.undraw()
              move_txt.undraw()

        #moves event to friday
        elif app.day(move_click) == 4:
          for i in friday.events:
            if IsInRect(move_click, i.rect):
              move_day(win, i)
              move_rect.undraw()
              move.undraw()

  #when the exit button is pressed and the loop ends, save all information to the file            
  write_to_file()
  

def move_day(win, event):
  #gives the user instructions on how to move their event
  move_day = Text(Point(0, 10), "What day would you like to move your event to?")
  move_day.setFace("helvetica")
  move_day2 = Text(Point(0, -10), "(Click the day)")
  move_day2.setFace("helvetica")
  move_day2.setStyle("italic")
  move_day.draw(win)
  move_day2.draw(win)
      
  p_day = win.getMouse()
  #delete old event
  event.delete_event(win)
  #saves mouseclick as a number to represent day [0,4]
  new_day = App.day(event, p_day)
  event.day_date = new_day
  #makes new event with new day
  event.make_event(win)
  event = event_to_day(event)

  move_day.undraw()
  move_day.undraw()
  move_day2.undraw()


def dayCopies(win,base_event,other_days):
  #makes a copy of base event iterating through the list and changing the Day
  i = 0
  for i in range (len(other_days)):
    new_event = Event(base_event.day_date, base_event.start_time, base_event.end_time, base_event.title, base_event.category)

    #changes day of copied event
    new_event.day_date = other_days[i]
    #draws to cal
    new_event.make_event(win)
    #adds new event to txt 
    e_txt = new_event.event_txt()
    event_to_day(new_event)
  

def event_to_day(event):
  #adds events to their corresponding day lists and day txt lists
  #monday
  if event.day_date == 0:
    monday.add_event(event)
    monday.add_eventtxt(event.event_txt())
  #tuesday
  elif event.day_date == 1:
    tuesday.add_event(event)
    tuesday.add_eventtxt(event.event_txt())
  #wednesday
  elif event.day_date == 2:
    wednesday.add_event(event)
    wednesday.add_eventtxt(event.event_txt())
  #thursday
  elif event.day_date == 3:
    thursday.add_event(event)
    thursday.add_eventtxt(event.event_txt())
  #friday
  elif event.day_date == 4:
    friday.add_event(event)
    friday.add_eventtxt(event.event_txt())


def daystr_to_num(day):
  #if given day in string form, returns the numerical version
  day_date = -1
  if day == "Monday":
    day_date = 0
  elif day == "Tuesday":
    day_date = 1
  elif day == "Wednesday":
    day_date = 2
  elif day == "Thursday":
    day_date = 3
  elif day == "Friday":
    day_date = 4
  return day_date

def write_to_file():
  #opens the file for writing
  f = open("saved_cal.txt", "w")

  #i is the list of each day's txt (the inner list of week_txt)
  #if i holds more than just the default day name, then write the contents of i to the file 
  for i in week_txt:
    if len(i) > 1:
      for j in i:
        f.write(j) 
      #gives each day its own line
      f.write("\n")

  f.close()
  return f

if __name__ == "__main__":
    main()


##REFERENCES: We used the IsInRect function (labeled rect_checker.py) from Joseph O'Rourke to simplify the process of making buttons