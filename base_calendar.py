from graphics import *
def make_base_calendar(win):
  #call calendar to create the calendar
  #ask user day, start time(hours), location, title, repeating (when)
  #call event class and create new instance
  #ask user if they want to add an event, edit event, delete event
    # Draw a frame/grids

  # line between monday and times
  p1 = Point(-82, 100)
  p2 = Point(-82, -100)
  line = Line(p1, p2)
  line.setWidth(1)
  line.setOutline('grey')
  line.draw(win)
  
  #line below all the weekday names
  p11 = Point(-100,90)
  p12 = Point(100,90)
  line5 = Line(p11, p12)
  line5.setWidth(1)
  line5.setOutline('grey')
  line5.draw(win)

  # line between MON and TUE
  p3 = Point(-45.6, 100)
  p4 = Point(-45.6, -100)
  line1 = Line(p3, p4)
  line1.setWidth(1)
  line1.setOutline('grey')
  line1.draw(win)

  # line between TUE and WED
  p5 = Point(-8.6, 100)
  p6 = Point(-8.6, -100)
  line2 = Line(p5, p6)
  line2.setWidth(1)
  line2.setOutline('grey')
  line2.draw(win)

  # line between WED and THU
  p7 = Point(27.8, 100)
  p8 = Point(27.8, -100)
  line3 = Line(p7, p8)
  line3.setWidth(1)
  line3.setOutline('grey')
  line3.draw(win)

  # line between THU and FRI
  p9 = Point(64.2, 100)
  p10 = Point(64.2, -100)
  line4 = Line(p9, p10)
  line4.setWidth(1)
  line4.setOutline('grey')
  line4.draw(win)

  #monday label
  MonText = Text(Point(-64, 95), "MON")
  MonText.draw(win)
  MonText.setTextColor('grey')

  #tuesday label
  TueText = Text(Point(-28, 95), "TUE")
  TueText.draw(win)
  TueText.setTextColor('grey')

  #wednesday label
  WedText = Text(Point(10, 95), "WED")
  WedText.draw(win)
  WedText.setTextColor('grey')

  #thursday label
  ThuText = Text(Point(46, 95), "THU")
  ThuText.draw(win)
  ThuText.setTextColor('grey')

  #friday label
  FriText = Text(Point(82, 95), "FRI")
  FriText.draw(win)
  FriText.setTextColor('grey')

  #text for each of the hours on the left hand side
  #midnight
  AMTwelveText = Text(Point(-91,86), "00:00")
  AMTwelveText.draw(win)
  AMTwelveText.setTextColor('grey')

  #1
  AMOneText = Text(Point(-91,78.4), "01:00")
  AMOneText.draw(win)
  AMOneText.setTextColor('grey')

  #2
  AMTwoText = Text(Point(-91,70.8), "02:00")
  AMTwoText.draw(win)
  AMTwoText.setTextColor('grey')

  #3
  AMThreeText = Text(Point(-91,63.2), "03:00")
  AMThreeText.draw(win)
  AMThreeText.setTextColor('grey')

  #4
  AMFourText = Text(Point(-91,55.6), "04:00")
  AMFourText.draw(win)
  AMFourText.setTextColor('grey')

  #5
  AMFiveText = Text(Point(-91,48), "05:00")
  AMFiveText.draw(win)
  AMFiveText.setTextColor('grey')

  #6
  AMSixText = Text(Point(-91,40.4), "06:00")
  AMSixText.draw(win)
  AMSixText.setTextColor('grey')

  #7
  AMSevenText = Text(Point(-91,32.8), "07:00")
  AMSevenText.draw(win)
  AMSevenText.setTextColor('grey')

  #8
  AMEightText = Text(Point(-91,25.2), "08:00")
  AMEightText.draw(win)
  AMEightText.setTextColor('grey')

  #9
  AMNineText = Text(Point(-91,17.6), "09:00")
  AMNineText.draw(win)
  AMNineText.setTextColor('grey')

  #10
  AMTenText = Text(Point(-91,10), "10:00")
  AMTenText.draw(win)
  AMTenText.setTextColor('grey')

  #11
  AMElevenText = Text(Point(-91,2.4), "11:00")
  AMElevenText.draw(win)
  AMElevenText.setTextColor('grey')

  #12
  PMTwelveText = Text(Point(-91,-5.2), "12:00")
  PMTwelveText.draw(win)
  PMTwelveText.setTextColor('grey')

  #13, 1PM
  PMOneText = Text(Point(-91,-12.8), "13:00")
  PMOneText.draw(win)
  PMOneText.setTextColor('grey')

  #14, 2PM
  PMTwoText = Text(Point(-91,-20.4), "14:00")
  PMTwoText.draw(win)
  PMTwoText.setTextColor('grey')

  #15, 3PM
  PMThreeText = Text(Point(-91,-28), "15:00")
  PMThreeText.draw(win)
  PMThreeText.setTextColor('grey')

  #16, 4PM
  PMFourText = Text(Point(-91,-35.6), "16:00")
  PMFourText.draw(win)
  PMFourText.setTextColor('grey')

  #17, 5PM
  PMFiveText = Text(Point(-91,-43.2), "17:00")
  PMFiveText.draw(win)
  PMFiveText.setTextColor('grey')

  #18, 6PM
  PMSixText = Text(Point(-91,-50.8), "18:00")
  PMSixText.draw(win)
  PMSixText.setTextColor('grey')

  #19, 7PM
  PMSevenText = Text(Point(-91,-58.4), "19:00")
  PMSevenText.draw(win)
  PMSevenText.setTextColor('grey')

  #20, 8PM
  PMEightText = Text(Point(-91,-66), "20:00")
  PMEightText.draw(win)
  PMEightText.setTextColor('grey')

  #21, 9PM
  PMNineText = Text(Point(-91,-73.6), "21:00")
  PMNineText.draw(win)
  PMNineText.setTextColor('grey')

  #22, 10PM
  PMTenText = Text(Point(-91,-81.2), "22:00")
  PMTenText.draw(win)
  PMTenText.setTextColor('grey')

  #23, 11PM
  PMElevenText = Text(Point(-91,-88.8), "23:00")
  PMElevenText.draw(win)
  PMElevenText.setTextColor('grey')

  #24, Midnight
  AMTwelveText = Text(Point(-91,-96.4), "24:00")
  AMTwelveText.draw(win)
  AMTwelveText.setTextColor('grey')
