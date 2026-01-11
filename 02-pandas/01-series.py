import pandas as pd

print(pd.__version__)

# Series = a pandas 1-dimensional labeled array that can hold any data type
#           Think of it like a single column in a spreadsheet (1 dimensional)


data = [100, 102, 104]
series = pd.Series(data, index=["a", "b", "c"])
print(series)
series.loc["c"] = 200
print(series.loc["a"]) #location at label
print(series)

#lock using integer

print(series.iloc[1])

print(series[series < 200])

#
calories = {"Day1": 1750,
            "Day2": 2100,
            "Day3": 1700}

series = pd.Series(calories)
print(series)
print(series.loc["Day1"])
print(series [series <2000])
