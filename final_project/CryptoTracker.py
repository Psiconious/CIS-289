import requests
import json
import csv
from pathlib import Path
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
import datetime
from datetime import date
from datetime import timedelta
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
Name: Trever Cluney
Date: 04/29/22
Email: tlcluney@dmacc.edu
Overview: Simple program for getting data about cryptocurrency
"""


class GameWindow:

    date1 = date.today() - timedelta(days=1)
    date2 = date.today()

    def __init__(self):
        # Create an instance of tkinter frame or window
        win = Tk()
        win.title("Calendar")
        win.geometry("700x600")

        # sets up date data
        self.cal = DateEntry(win, width=16, background="magenta3", foreground="white", bd=2, maxdate=date.today() - timedelta(days=1))
        self.cal.pack(pady=5)
        self.cal2 = DateEntry(win, width=16, background="magenta3", foreground="white", bd=2, maxdate=date.today())
        self.cal2.pack(pady=5)

        # Define Function to select the date
        def get_date():
            label.config(text=self.cal.get_date())
            label2.config(text=self.cal2.get_date())
            self.date1 = self.cal.get_date()
            self.date2 = self.cal2.get_date()

        # Create a button to pick the date from the calendar
        button = Button(win, text="Select the Date", command=get_date)
        button.pack(pady=5)
        # Create a button to get data from the api
        button = Button(win, text="Get Crypto Data from Dates", command=lambda: self.get_crypto_data())
        button.pack(pady=5)
        button = Button(win, text="Display Data", command=lambda: self.display_graph())
        button.pack(pady=5)

        # Create Label for displaying selected Date
        label = Label(win, text="")
        label.pack(pady=5)
        label2 = Label(win, text="")
        label2.pack(pady=5)

        win.mainloop()

    def display_graph(self):
        # checks if the file exist
        if Path('crypto_file.csv').is_file():
            # grabs important data to use for plotting
            crypto_csv = pd.read_csv('crypto_file.csv')
            unformatted_dates = crypto_csv['time_open'].to_numpy()
            crypto_high = crypto_csv['high'].to_numpy()
            crypto_low = crypto_csv['low'].to_numpy()
            crypto_open = crypto_csv['open'].to_numpy()
            crypto_close = crypto_csv['close'].to_numpy()
            # to set up formatted dates
            dates = []
            # loops though the numpy array
            for x in unformatted_dates:
                dates.append(datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ').strftime("%m/%d/%Y"))
            # plots data
            plt.plot(dates, crypto_open, label='Open amount')
            plt.plot(dates, crypto_close, label='Close amount')
            plt.plot(dates, crypto_high, label='High amount')
            plt.plot(dates, crypto_low, label='Low amount')
            # dynamic title
            plt.title('BitCoin Prices from ' + dates[0] + ' to ' + dates[-1])
            # tries to make xticks more readable
            plt.xticks(rotation=90)
            # gives a legend
            plt.legend()
            # displays plot
            plt.show()
            plt.close()
        else:
            # error message for when data doesnt exist
            messagebox.showinfo("No Data", "No Data File Found Select time frame to pull from")
        pass

    def get_crypto_data(self):
        # API call to grab data from timeframe given
        response = requests.get('https://api.coinpaprika.com/v1/coins/btc-bitcoin/ohlcv/historical?start='+str(self.date1)+'&end='+str(self.date2))
        # converts response text into json
        response_text = json.loads(response.text)
        # Opens/Creates a new file for writing to
        data_file = open('crypto_file.csv', 'w', newline='')
        # Creates a CSV writer
        csv_writer = csv.writer(data_file)
        # Counter to write the header
        count = 0
        # a for loop to get through all the data
        for data in response_text:
            # checks if the header has been written yet
            if count == 0:
                # assigns all keys as a header variable
                header = data.keys()
                # Writes header to file
                csv_writer.writerow(header)
                # updates counter
                count += 1
            # Writes the values from the json object
            csv_writer.writerow(data.values())
        # Closes file when finished
        data_file.close()
        pass


if __name__ == '__main__':
    GameWindow()
    pass
