import pandas as pd

name = input("Name? ")

df = pd.read_csv(name + '.csv')

df.dropna(subset=['eeg_2'], inplace=True)

df.to_csv('new' + name + '.csv', index=False)
