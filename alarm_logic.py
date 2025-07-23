import datetime
import time

# Alarm function
def alarm(set_alarm_time):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Current time:", current_time)
        if current_time == set_alarm_time or current_time == "00:00:00":
            print("Time to Wake up!")
            break

def get_valid_time_input():
    while True:
        user_input = input("Enter alarm time in HH:MM:SS format (24-hour): ")
        try:
            time.strptime(user_input, "%H:%M:%S")
            return user_input
        except ValueError:
            print("Invalid format. Please try again.")

