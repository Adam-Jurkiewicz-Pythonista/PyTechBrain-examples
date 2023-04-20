from datetime import datetime
from sys import exit
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from random import randrange
from PyTechBrain import *


board = PyTechBrain()
if not board.board_init():
    print("Nie mogę połączyć z płytką!")
    exit

x_data, y_data = [], []
figure = pyplot.figure()
line, = pyplot.plot_date(x_data, y_data, '-')

def function_returns_data():
    return board.get_fotoresistor_raw()


def update(frame):
    x_data.append(datetime.now())
    y_data.append(function_returns_data())
    line.set_data(x_data, y_data)
    figure.gca().relim()
    figure.gca().autoscale_view()
    return line,

animation = FuncAnimation(figure, update, interval=200)

pyplot.show()