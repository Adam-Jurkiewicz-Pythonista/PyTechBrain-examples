from PyTechBrain import  *
from time import sleep

board = PyTechBrain(debug=True)

print(board.license_info())


board.board_init()

# print(board.com_list)

while True:
    board.set_signal_red("on")
    sleep(0.5)
    board.set_signal_yellow("on")
    sleep(0.5)
    board.set_signal_red("off")
    board.set_signal_yellow("off")
    board.set_signal_green("on")
    sleep(0.8)