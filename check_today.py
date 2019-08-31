import os
import time
import numpy as np
import pandas as pd
from os.path import join
from datetime import datetime, timedelta


def get_birthdays(df, day, year):
    df_copy = df.copy()
    df_copy["ages"] = year - df_copy["birthyear"]
    birthdays = df_copy.loc[df_copy.birthday == day]
    return birthdays

def format_notification(birthdays, message):
    for person in birthdays.values:
        name = person[0]
        age  = person[3]

        message.append(name)
        if not np.isnan(age):
            message.append(f" - {int(age)} yrs old")
        message.append("\n")
    return message

def get_notification(dates, year):
    message = list()

    for name, date in dates:
        birthdays = get_birthdays(df, date, year)
        if len(birthdays) != 0:
            message.append("%s's Birthdays\n" % name)
            message = format_notification(birthdays, message)
            message.append("\n")

    return "".join(message)

if __name__ == "__main__":
    root = "/Users/pbezuhov/git/Birthdays"
    csv  = join(root, "birthdays.csv")
    df   = pd.read_csv(csv)

    today, year = time.strftime("%-d %B"), int(time.strftime("%Y"))
    dates = [ ("Today", today) ]
    for day_offset in range(1, 10):
        day = (datetime.strptime(today, "%d %B") + timedelta(days=day_offset)).strftime("%-d %B")
        dates.append( ("%d day from now" % day_offset, day) )

    message = get_notification(dates, year)
    print(message)

