from graphics import *

class Event:
  def __init__(self, day_date, start_time, end_time, title, category, color = 'orange', event_type = None):
    #initiates all of the different parts of the event class
    self.day_date = day_date
    self.start_time = start_time
    self.end_time = end_time
    self.title = title
    self.category = category
    self.color = color

    #holds lines so we can split the text of the event into rows so it fits nicely into the box
    self.lines = []
    #allows the program to return the rect so it can be moved etc
    self.rect = None


  def print(self):
    #mostly helpful for debugging. kept if we ever want to add to the program. just prints the contents of the event class in a readable way
    print(self.title, "is on", self.day_date, "from", self.start_time,"to", self.end_time)


  def day(self, day):
    #tells the program where to draw the vertical lines for events based on what day they are
    day_points = []
    #monday points
    if day == 0: 
      day_points = [-82, -45.6]
    #tuesday points
    elif day == 1:
      day_points = [-45.6, -8.6]
    #wednesday points
    elif day == 2:
      day_points = [-8.6, 27.8]
    #thursday points
    elif day == 3:
      day_points = [27.8, 64.2]
    #friday points
    elif day == 4:
      day_points = [64.2, 100]
    return day_points


  def time (self, time): 
    #takes the hour time given [0,24] and gives it a corresponding y value approximately where that hour is on the calendar
    #to help place the event on the calendar
    y = None
    if time == 0:
      y = 86
    elif time == 1:
      y = 78.4
    elif time == 2:
      y = 70.8
    elif time == 3: 
      y = 63.2
    elif time == 4:
      y = 55.6
    elif time == 5:
      y = 48
    elif time == 6:
      y = 40.4
    elif time == 7:
      y = 32.8
    elif time == 8:
      y = 25.2
    elif time == 9:
      y = 17.6
    elif time == 10:
      y = 10
    elif time == 11:
      y = 2.4
    elif time == 12:
      y = -5.2 ##base case
    elif time == 13:
      y = -12.8
    elif time == 14:
      y = -20.4
    elif time == 15: 
      y = -28
    elif time == 16:
      y = -35.6
    elif time == 17:
      y = -43.2
    elif time == 18:
      y = -50.8
    elif time == 19:
      y = -58.4
    elif time == 20:
      y = -66
    elif time == 21:
      y = -73.6
    elif time == 22:
      y = -81.2
    elif time == 23:
      y = -88.8
    elif time == 24:
      y = -96.4
    return y


  def count_text(self,title):
    #makes the title a list of characters to count them
    characters = list(title)
    char_count = len(characters)
    return char_count
    

  def place_text(self, title):
    #parse title text and determine the number of lines based on the number of characters
    title_count = self.count_text(self.title)
    num_lines = 0
    if 30 > title_count > 15:
      num_lines = 2
    elif title_count >= 31:
      num_lines = 3
    elif title_count <= 15:
      num_lines = 1
    return num_lines


  def color_selection(self, category):
    #determines the color of the box based on what category the event is
    if self.category == 'work':
      self.color = color_rgb(245, 213, 203)
    elif self.category == 'school':
      self.color = color_rgb(213, 214, 234)
    elif self.category == 'social':
      self.color = color_rgb(215, 236, 217)
    return self.color

  def make_event(self, win):
    #draws the event to calendar

    #makes y coordinates of rectangle (top and bottom)
    y1 = self.time(self.start_time)
    y2 = self.time(self.end_time)

    #makes x coordinates of rectangle (left and right)
    day_points = self.day(self.day_date)
    x1 = day_points[0]
    x2 = day_points[1]
    day_left = Point(x1,y2)
    day_right = Point(x2,y1)
    self.rect = Rectangle(day_left, day_right)

    #sets color of rectangle
    set_color = self.color_selection(self.category)
    self.rect.setFill(set_color)
    self.rect.draw(win)
    mid_x = (x1 + x2)/2
    mid_y = (y1 + y2)/2

    #creates a list of the event title and counts the characters
    list_title = list(self.title)
    title_count = self.count_text(self.title)
    line_count = self.place_text(self.title)
    
    #determines the number of lines needed for the event title and draws them in the correct event rectangle
    if line_count == 1:
      #draws 1 line
      line1 = ('').join(list_title)
      first_line = Text(Point(mid_x, mid_y), line1)
      first_line.draw(win)
      self.lines.append(first_line)

    elif line_count == 2:
      #draws 2 lines
      line1 = ('').join(list_title[:16])
      line2 = ('').join(list_title[16:])

      first_line = Text(Point(mid_x, mid_y + 5), line1)
      first_line.draw(win)
      self.lines.append(first_line)

      sec_line = Text(Point(mid_x, mid_y), line2)
      sec_line.draw(win)
      self.lines.append(sec_line)

    elif line_count == 3:
      #draws 3 lines
      line1 = ('').join(list_title[:16])
      line2 = ('').join(list_title[16:31])
      line3 = ('').join(list_title[31:])

      first_line = Text(Point(mid_x, mid_y + 5), line1)
      first_line.draw(win)
      self.lines.append(first_line)

      sec_line = Text(Point(mid_x, mid_y), line2)
      sec_line.draw(win)
      self.lines.append(sec_line)

      thr_line = Text(Point(mid_x, mid_y - 5), line3)
      thr_line.draw(win)
      self.lines.append(thr_line)

  def event_txt(self):
    #formats the event information in the format it will be saved to the file
    txt =str(self.start_time) + "-" + str(self.end_time) + "-" + self.title  + "-" + self.category + ","
    return txt


  def delete_event(self, win):
    #deletes the event
    self.rect.undraw()
    for i in self.lines:
      i.undraw()

    
