from tkinter import *
from threading import Thread
from alarm_logic import alarm, get_valid_time_input

def main():
    print("Alarm Clock (CLI Version)")
    alarm_time = get_valid_time_input()
    print(f"Alarm set for {alarm_time}")
    
    t = Thread(target=alarm, args=(alarm_time,))
    t.start()
    t.join()

if __name__ == "__main__":
    main()
