import numpy as np
import pandas as pd

PATH = "/Users/pbezuhov/git/Birthdays/"

df = pd.read_csv(PATH + "birthdays.csv")
df = df.sort_values("name", ascending=True)
df.to_csv(PATH + "birthdays.csv", index=False)
