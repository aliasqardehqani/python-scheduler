import sched
import time
from datetime import datetime

def print_on():
    print("ON")

def print_off():
    print("OFF")

def schedule_tasks_start(date, start_time):
    s = sched.scheduler(time.time, time.sleep)
    datetime_format = "%Y-%m-%d %H:%M:%S"
    start_datetime = datetime.strptime(f"{date} {start_time}", datetime_format)
    start_timestamp = time.mktime(start_datetime.timetuple())
    s.enterabs(start_timestamp, 1, print_on, ())
    s.run()


def schedule_tasks_end(date, end_time):
    s = sched.scheduler(time.time, time.sleep)
    datetime_format = "%Y-%m-%d %H:%M:%S"
    end_datetime = datetime.strptime(f"{date} {end_time}", datetime_format)
    end_timestamp = time.mktime(end_datetime.timetuple())
    s.enterabs(end_timestamp, 2, print_off, ())
    s.run()


# # date = "2024-01-02"
# # start_time = "13:53:00"
# # end_time = "13:53:40"

# # Schedule tasks
# schedule_tasks_start(date, start_time)
# schedule_tasks_end(date, end_time)
