import pandas as pd
import sys

for file in [sys.argv[i] for i in range(len(sys.argv)) if i != 0]:

    NAME = file
    #NAME = "alexcontrol"

    print(f"Reading file: {NAME}")
    df = pd.read_csv(f'{NAME}')

    new_df = df[(df["eeg_1"].isnull() | df["eeg_2"].isnull()) == False]
    #new_df = df[(df["eeg_1"].str is None or df["eeg_2"].str is None) == False]

    #new_df = df.dropna()

    new_df.to_csv(f"./cooked_{NAME}")
    print(f"saved file: cooked_{NAME}")

