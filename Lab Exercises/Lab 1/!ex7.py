# Write a Pandas program to create a time-series from a given list of dates as strings and save them in a file.

# timeSeries = ['a', 'b', 'c', 'd', 'e']

# textFile = open("time-series.txt", "w")


# for i in timeSeries:
#     textFile.write(f"{i} \n")

# textFile.close()


import pandas as pd

# Create a list of dates as strings
dates = ["2023-10-04", "2023-10-05", "2023-10-06", "2023-10-07", "2023-10-08"]

# Create a time series
ts = pd.Series(dates)

# Save the time series to a text file
with open("time_series.txt", "w") as f:
    f.write(ts.to_string())
