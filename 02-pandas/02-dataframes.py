import pandas as pd

# dataframe = a tabular data structure with rows and columns. (2 dimensional)
#               similar to an excel spreadsheet

data = {
    "Name":["Spongebob","Patrick","Squidward"],
    "Age":[30,35,50]
        }

#constructor "DataFrame"
df = pd.DataFrame(data, index = [1,2,3])
print(df)

#access row
print(df.iloc[1])

#add a new column

print()
df["Job"]=["Cook", "N/A", "Cashier"]
print(df)

#add new rows
print()

new_rows = pd.DataFrame([{"Name": "Sandy","Age":28,"Job":"Engineer"},
                         {"Name": "Ash","Age":25,"Job":"Engineer"}], index=[4,5])
df=pd.concat([df,new_rows])

print(df)