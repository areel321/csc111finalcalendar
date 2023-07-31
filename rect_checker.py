from graphics import *
from app import *

def IsInRect( p, rect ):
    """Is point p inside the rectangle?
       Both p and rect are graphics objects.
    """
    # Extract the pt coords:
    x,y = p.getX(),p.getY()

    # Extract the rect corners:
    p1 = rect.getP1()
    x1,y1 = p1.getX(),p1.getY()
    p2 = rect.getP2()
    x2,y2 = p2.getX(),p2.getY()

    # Inside the rect when between both x&y.
    # Make no assumption about p1 & p2, so need to 
    # check several between possibilities.
    if ((x1 <= x <= x2) or (x1 >= x >= x2)) and ((y1 <= y <= y2) or (y1 >= y >= y2)):
        # if trace:
        #   print('IsInRect')
        return True
    else:
        return False