import pandas as pd

import matplotlib.pyplot as plt

'''
The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.

The number varies from -1 to 1.

1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column,
 the other one went up as well.

0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.

-0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.

0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.

'''

df = pd.read_csv("cor_data.csv")

d = df.dropna()
d.drop_duplicates()
print(d)
print(d.corr())


#Plot some graphs 
#d.plot()
#scater plot
#d.plot(kind="scatter",x="Pulse",y="Calories")

# histogram
#Note: The histogram tells us that there were over 100 workouts that lasted between 50 and 60 minutes.

d["Duration"].plot(kind="hist")


plt.show()
