"""
Name: Trever Cluney
Date: 02.07.2022
Email: tlcluney@dmacc.edu
Overview: Using pandas to preform SQL data queries manipulations
"""
import pandas as pd
daily_temp = pd.read_csv("daily_temp.txt", sep=',', index_col='days_of_the_week')
print(daily_temp)
print(daily_temp.dtypes)
daily_snow = pd.read_csv("daily_precip_and_snow.txt", sep=',', index_col='days_of_the_week')
print(daily_snow)
daily_merged = daily_temp.merge(daily_snow, how='left', on=['days_of_the_week'])
print(daily_merged)
daily_merged['max_temp'] = ((daily_merged['max_temp'] - 32) * (5/9))
daily_merged['min_temp'] = ((daily_merged['min_temp'] - 32) * (5/9))
print(daily_merged)
daily_merged['avg_temp'] = (daily_merged['max_temp'] + daily_merged['min_temp']) / 2
print(daily_merged)
daily_merged = daily_merged.reindex(columns=['max_temp', 'min_temp', 'avg_temp', 'precipitation', 'new_snow'])
print(daily_merged)
