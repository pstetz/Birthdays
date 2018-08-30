import numpy as np
import pandas as pd

df = pd.read_csv("birthdays.csv")
df = df.sort_values("name", ascending=True)
df.to_csv("birthdays.csv", index=False)
