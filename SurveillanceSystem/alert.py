import datetime
import os
import platform

def trigger_alert():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 500)
    elif platform.system() == "Darwin":  
        os.system('say "Alert!"')
    else:  
        os.system('paplay /usr/share/sounds/freedesktop/stereo/complete.oga')

def log_event(event):
    with open("log.csv", "a") as f:
        f.write(f"{datetime.datetime.now()},{event}\n")
