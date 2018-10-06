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

To fix:
-when printing out seconds it doesn't lists 1-9 isntead of 01-09
-format pomodoro_timer/short_break/long_break to have a consistant
 output
-Single function call to print to screen
'''

#imports
from datetime import datetime
from datetime import timedelta
import time
import sys

def pomodoro_timer(task_name='my_task'):
    ''' A pomodoro task timer that takes a task name'''

    #define starting and ending times
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=25*60)


    while datetime.now() < end_time:
        current_time = datetime.now()
        time_left = end_time-current_time
        sys.stdout.write("\r")
        sys.stdout.write('Task: {} Timeleft: {}:{} '.format(task_name, int(time_left.seconds / 60), time_left.seconds % 60))
        sys.stdout.flush()
        time.sleep(1)

def short_break(duration = 3):
    ''' A short break timer that takes a duration between 3-5
        minutes'''
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=duration)

    while datetime.now() < end_time:
        current_time = datetime.now()
        time_left = end_time-current_time
        sys.stdout.write("\r")
        sys.stdout.write('Short Break Timeleft: {}:{} '.format(int(time_left.seconds / 60), time_left.seconds % 60))
        sys.stdout.flush()
        time.sleep(1)

def long_break(duration = 15):
    ''' A long break timer that takes a duration between 15-30
        minutes'''
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=duration)

    while datetime.now() < end_time:
        current_time = datetime.now()
        time_left = end_time-current_time
        sys.stdout.write("\r")
        sys.stdout.write('Long Break Timeleft: {}:{} '.format(int(time_left.seconds / 60), time_left.seconds % 60))
        sys.stdout.flush()
        time.sleep(1)


if __name__ == "__mai
n__":
    #pomodoro_timer()
    long_break()
