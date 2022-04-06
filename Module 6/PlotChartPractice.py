import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
"""Name: Trever Cluney"""
plt.style.use('fivethirtyeight')

steam_games = pd.read_csv('steam.csv', sep=',', index_col='appid')

game_ratings = steam_games.loc[:, ['publisher', 'name', 'positive_ratings', 'negative_ratings']]
game_ratings['total_ratings'] = game_ratings['positive_ratings'] + \
                                game_ratings['negative_ratings']

publisher_game_ratings = game_ratings.loc[:, ['publisher', 'total_ratings']]
publisher_game_ratings = publisher_game_ratings.groupby('publisher')['total_ratings'].sum()
publisher_game_ratings = publisher_game_ratings.reset_index()

publisher_game_positive_ratings = game_ratings.loc[:, ['publisher', 'positive_ratings']]
publisher_game_positive_ratings = publisher_game_positive_ratings.groupby('publisher')['positive_ratings'].sum()
publisher_game_positive_ratings = publisher_game_positive_ratings.reset_index()

publisher_game_negative_ratings = game_ratings.loc[:, ['publisher', 'negative_ratings']]
publisher_game_negative_ratings = publisher_game_negative_ratings.groupby('publisher')['negative_ratings'].sum()
publisher_game_negative_ratings = publisher_game_negative_ratings.reset_index()

complete_publisher_ratings = pd.merge(publisher_game_positive_ratings, publisher_game_negative_ratings, on='publisher')
complete_publisher_ratings = pd.merge(complete_publisher_ratings, publisher_game_ratings, on='publisher')
complete_publisher_ratings = complete_publisher_ratings.sort_values('total_ratings', ascending=False)

negative_ratings = complete_publisher_ratings['negative_ratings'].head(10).to_numpy()
positive_ratings = complete_publisher_ratings['positive_ratings'].head(10).to_numpy()
total_ratings = complete_publisher_ratings['total_ratings'].head(10).to_numpy()
publisher_name = complete_publisher_ratings['publisher'].head(10).to_numpy()

x_indexes = np.arange(len(publisher_name))
width = 0.25

plt.ticklabel_format(style='plain')
plt.bar(x_indexes, total_ratings, color='#444444', width=width, label='Total Ratings')

plt.bar(x_indexes - width, negative_ratings, color='#ff0000', width=width, label='Negative Ratings')

plt.bar(x_indexes + width, positive_ratings, color='#0000ff', width=width, label='Positive Ratings')

current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

plt.legend()

plt.xticks(ticks=x_indexes, labels=publisher_name, rotation=50)
plt.gca().tick_params(axis='x', labelsize=7)

plt.title('Top 10 Highest Rated Publishers (on steam)')
plt.xlabel('Publishers')
plt.ylabel('Ratings')

plt.tight_layout()

plt.show()
