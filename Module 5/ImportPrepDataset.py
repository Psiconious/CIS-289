"""
Name: Trever Cluney
Date: 2.14.22
Email: tlcluney@dmacc.edu
Overview: using pandas to preform data manipulation on the steam game service
"""
import pandas as pd
steam_games = pd.read_csv('steam.csv', sep=',', index_col='appid')
publisher_positive_reviews = steam_games[steam_games['positive_ratings'] >= 50].loc[:, ['publisher', 'positive_ratings', 'negative_ratings']]
publisher_positive_reviews = publisher_positive_reviews.groupby('publisher')
publisher_positive_reviews = publisher_positive_reviews.sum()
print(publisher_positive_reviews)
rows_to_kick = steam_games[steam_games['positive_ratings'] < 50].index
steam_games = steam_games.drop(rows_to_kick)
steam_games['total_ratings'] = steam_games['positive_ratings'] + steam_games['negative_ratings']
fifty_reviews = steam_games[steam_games['total_ratings'] >= 50]
fifty_reviews.sort_values(by=['positive_ratings'], ascending=False, inplace=True)
print(fifty_reviews.describe())
print(fifty_reviews.iloc[:, 1:14])
fifty_reviews = fifty_reviews[fifty_reviews['owners'] != '0-20000']
print(fifty_reviews.loc[:, ['name', 'owners', 'total_ratings']])

