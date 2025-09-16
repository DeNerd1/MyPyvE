import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print(df)

#Locate Row
print(df.loc[0])


#Load Files Into a DataFrame

readfile = pd.read_csv('data.csv')
print(readfile.to_json())
print(readfile.to_string())

print("Get max rows resturn by the system")
# increase the rows
pd.options.display.max_rows =100
print(pd.options.display.max_rows)

print("read json ")
js = pd.read_json("data.json")
print(js.to_csv())

#Viewing the Data

print(js.head(2))

print(js.tail(1))

print("info ------------------")
print(js.info())