import time

from constants import *


def run_program():
    print(Programmer)
    time.sleep(7)
    run_program()

run_program()
