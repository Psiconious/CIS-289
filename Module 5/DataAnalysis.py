"""
Name: Trever Cluney
Date: 2.14.22
Email: tlcluney@dmacc.edu
Overview: using pandas to preform data manipulation on the steam game service
"""
import pandas as pd
steam_games = pd.read_csv('steam.csv', sep=',', index_col='appid')
owners_to_ratings = steam_games.loc[:, ['owners', 'positive_ratings', 'negative_ratings']]
owners_to_ratings = owners_to_ratings.groupby('owners')
owners_to_ratings = owners_to_ratings.sum()
print(steam_games.groupby('owners')['positive_ratings'].value_counts(normalize=True)*100)

