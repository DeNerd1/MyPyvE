import pandas as pd

print('ok')
df = pd.read_csv("clean_data.csv")
print(df)

print('------------------------------------------')
# remove emty cells or n/a
new_df = df.dropna()
#print(new_df)

# Remove all rows with NULL values with inplace 

#df.dropna(inplace=True)
#print(df.to_string())

#The fillna() method allows us to replace empty n/a cells with a value
df.fillna(130, inplace = True)
print(df.to_string())

#Replace Using Mean, Median, or Mode
x = df["Calories"].mean()
print(x)
df.fillna({"Calories": x}, inplace=True)
print(df)

#fix date wrong format
print('date----------------------------------')
date = pd.read_csv("clean_data.csv")
date['Date'] = pd.to_datetime(date["Date"],format='mixed')
print(date)
# drop the date if can't fix 
df.dropna(subset=['Date'], inplace = True)
print(df)

#remove dublicates

print(df.duplicated())
print(df.drop_duplicates())