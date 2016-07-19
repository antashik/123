from turtle import Turtle
t = Turtle()
def test_drawmav():
    pen_down()
    for i in range (5):
        on_vector(1,2)
        on_vector(0,-2)
    pen_up()
    to_point(0,0)

def pen_dowv():
    pass

def pen_up():
    pass

def on_vector():
    pass

def to_point(x,y):
    pass

if __name__=='__main__':
    test_drawman ()