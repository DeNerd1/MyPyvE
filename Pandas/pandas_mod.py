
'''
Pandas gives you answers about the data. Like:

Is there a correlation between two or more columns?
What is average value?
Max value?
Min value?

'''

import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"], 'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)


print('hehe')
a =[[20,34,23,29,300],[23,24,21,211,34]]
d = pandas.DataFrame(a)
print(d)
print(d[0])

# series

print("Data series ")
s = [20,34,300]
ds = pandas.Series(s)
print(ds)
print("Index :",ds[0])

#Create Labels with indexes

print("label with indexes ")
label = pandas.Series(s, index=["x","y","z"])
print(label)
print(label['z'])

#Key/Value Objects as Series
print("key value objects")
calories = {"day1": 420, "day2": 380, "day3": 390}
cal = pandas.Series(calories)
print(cal)

update = pandas.Series(calories,index=["day1","day2"])
print(update)
