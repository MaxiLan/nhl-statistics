import pandas as pd

games = pd.read_parquet("data/games.parquet")

# print(games.head())
print(games.shape)
print(games.tail())
print(games.columns)
print(games.iloc[-1,:])