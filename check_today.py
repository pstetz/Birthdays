import numpy as np
import pandas as pd
import time
from datetime import datetime, timedelta

import warnings
warnings.filterwarnings('ignore')

PATH = "/Users/pbezuhov/git/Birthdays/"
df = pd.read_csv(PATH + "birthdays.csv")

def get_birthdays(df, day, year):
    birthdays = df[df.birthday == day]
    birthdays["ages"] = year - birthdays.birthyear
    return birthdays

def format_notification(birthdays, message):
    if len(birthdays) == 0:
        message.append("None")
        return message
    for person in birthdays.values:
        name = person[0]
        age  = person[3]
        
        message.append(name)
        if not np.isnan(age):
            message.append(f" - {int(age)} yrs old")
        message.append("\n")
    return message

def get_notification(today, tomorrow, year):
    ### Today
    message = list("Today's Birthdays\n")
    birthdays_today = get_birthdays(df, today, year)
    message = format_notification(birthdays_today, message)
    
    ### Tomorrow
    message.append("\n")
    message.append("Tomorrow's birthdays\n")
    birthdays_tomorrow = get_birthdays(df, tomorrow, year)
    message = format_notification(birthdays_tomorrow, message)

    if len(birthdays_today) + len(birthdays_tomorrow) != 0:
        return "".join(message)
    return "None"

if __name__ == "__main__":
    today, year = time.strftime("%-d %B"), int(time.strftime("%Y"))
    tomorrow = (datetime.strptime(today, "%d %B") + timedelta(days=1)).strftime("%-d %B")
    message  = get_notification(today, tomorrow, year)
    print(message)

