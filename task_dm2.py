from drawman import *
from time import sleep
drawman_draw_grid ('blue')
t.pencolor('black')
def f(x):
    return x*x
drawman_scale(50)
x=-5.0
to_point(x,f(x))
pen_down()
while x<=5:
    to_point(x,f(x))
    x +=0.1
pen_up()
sleep (5)
