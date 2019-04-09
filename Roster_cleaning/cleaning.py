import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_csv("ROSTERS.csv")

#df.drop_duplicates(subset=None, inplace=True)
df = df.loc[df['Employee ID'] != 'Employee ID']

df = df[:-1]

df['Employee ID'] = df['Employee ID'].astype(int)

df = df.loc[df['Employee ID'] >= 15000000]

df['Date'] = pd.to_datetime(df['Date'],format='%d/%m/%Y')
df['Date'] = df['Date'].dt.strftime('%Y%m%d')

df.to_csv('ROSTER_OUT.csv',header=False, index=False,)
