from event import *
class Day: 
  def __init__(self, name):
    #creates a list of events for each day

    #string that will be the first element of the events_txt list that holds the name of each day with an asterisk after
    self.name = None

    #events list holds the event objects for each day
    self.events = []
    #events txt list holds the txt for events of each day to write to the file
    self.events_txt = [name]

  def add_event(self, event):
    #adds events to the list
    self.events.append(event) 
    return self.events


  def add_eventtxt(self, txt):
    #list of the text outputs for saving to file
    self.events_txt.append(txt)


  def delete_event(self,event):
    #removes event from the list
    self.events.remove(event)
    return self.events

