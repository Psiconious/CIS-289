import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""Name: Trever Cluney"""

plt.style.use('fivethirtyeight')

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True)

#importing data set for iowa
iowa_weather_data = pd.read_csv('iowa_dataset.csv')
#importing data set for texas
texas_weather_data = pd.read_csv('texas_dataset.csv')
#grabbing data from the first station
iowa_weather_data = iowa_weather_data.loc[iowa_weather_data['STATION'] == 'USC00135650']
#grabbing data from the second station
texas_weather_data = texas_weather_data.loc[texas_weather_data['STATION'] == 'USW00003951']

dates = iowa_weather_data['DATE'].to_numpy()

iowa_daily_precipitation = iowa_weather_data['DLY-PRCP-PCTALL-GE001HI'].to_numpy()
iowa_daily_snow = iowa_weather_data['DLY-SNOW-PCTALL-GE001TI'].to_numpy()

texas_daily_precipitation = texas_weather_data['DLY-PRCP-PCTALL-GE001HI'].to_numpy()
texas_daily_snow = texas_weather_data['DLY-SNOW-PCTALL-GE001TI'].to_numpy()

ax1.plot(dates, iowa_daily_precipitation, linestyle='--', label='precipitation')
ax1.plot(dates, iowa_daily_snow, linestyle='-', label='snow')

ax2.plot(dates, texas_daily_precipitation, linestyle='--', label='precipitation')
ax2.plot(dates, texas_daily_snow, linestyle='-', label='snow')

ax1.legend()
ax2.legend()

# Rotating X-axis labels
ax2.set_xticklabels(dates, rotation = 50)

ax1.set_title('Iowa and Texas Precipitation and Snow (in January)')
ax1.set_ylabel('Percents')
ax2.set_xlabel('Days of the month')

plt.tight_layout()

plt.show()
