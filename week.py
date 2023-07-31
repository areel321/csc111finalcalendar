from day import *

class Week:
  def __init__(self, monday, tuesday, wednesday, thursday, friday):
    #holds the 5 days of the week
    self.monday = monday
    self.tuesday = tuesday
    self.wednesday = wednesday
    self.thursday = thursday
    self.friday = friday

    self.days_of_week = [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday]
    ##list of days of the week


  def days_txt(self):
    #the list that contains all of the txt that will be written to the file to save
    week_txt = [monday.events_txt, tuesday.events_txt, wednesday.events_txt, thursday.events_txt, friday.events_txt]
    


