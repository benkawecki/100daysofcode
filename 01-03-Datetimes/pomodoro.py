'''
Ben Kawecki

Pomodoro Timer

from https://en.wikipedia.org/wiki/Pomodoro_Technique

1) Decide on the task to be done.
2) Set the pomodoro timer (traditionally to 25 minutes).[1]
3) Work on the task.
4) End work when the timer rings and put a checkmark on a piece of paper.[5]
5) If you have fewer than four checkmarks, take a short break (3–5 minutes), then go to step 2.
6) After four pomodoros, take a longer break (15–30 minutes), reset your checkmark count to zero, then go to step 1.



Features to be written:
-logging function to record tasks done and times worked on
-cmd line interface
-gui? (possibly)


'''

#imports
from datetime import datetime
from datetime import timedelta
import time
import sys

def pomodoro_timer():
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=25*60)

    while datetime.now() < end_time:
        current_time = datetime.now()
        time_left = end_time-current_time
        sys.stdout.write("\r")
        sys.stdout.write('The time is now {} and there are {} minutes and {} seconds left until the end of this pomodoro'.format(current_time, int(time_left.seconds / 60), time_left.seconds % 60))
        sys.stdout.flush()
        time.sleep(1)
    pass

def short_break():
    pass

def long_break():
    pass

if __name__ == "__main__":
    pomodoro_timer()
