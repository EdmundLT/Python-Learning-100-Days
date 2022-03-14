## #This is all project from Day71 - Day80

Proeject List in order by Learning Day:

1.

## Concepts Used in Day71 - Day80

## Ipynb (Google Colaboratory) using pandas Day 1

```
import pandas as pd

df = pd.read_csv("csv_example.csv")
df.head() <- read the head
df.shape <- column and row numbers
df.tail() <- read the tail
clean_df['Starting Median Salary'] <- show only column
clean_df['Starting Median Salary'].max() <- find the max item in specific column

1. clean_df['Starting Median Salary'].idxmax() <- find which row are max in Starting Median Salary
2. clean_df['Undergraduate Major'].loc[43] <- find the "Undergraduate Major" in specific row
3. clean_df.loc[43] <- whole row of 43

clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
= 90th / 10th

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col) <- insert one more column named 'Spread' which equal to srpead_col,
clean_df.head()

low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()

sort from low to high
print a table only with 2 columns(Spread, Undergraduate Major)


```

Exercise:
Use this CSV:

1. Using the .sort_values() method, can you find the degrees with the highest potential? Find the top 5 degrees with the highest values in the 90th percentile.

2. Also, find the degrees with the greatest spread in salaries. Which majors have the largest difference between high and low earners after graduation.

Answer:

```
highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()
** Major with the Highest Potential**
```

highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

```
**Majors with the Greatest Spread in Salaries**
```

highest_spread = clean_df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']].head()

```
mean() and count()
```

clean_df.groupby('Group').mean() = Average
clean_df.groupby('Group').count() = number of row

```
formatting
```

pd.options.display.float_format = '{:,.2f}'.format


## Summary of Day 1
1. Use .head(), .tail(), .shape and .columns to explore your DataFrame and find out the number of rows and columns as well as the column names.

2. Look for NaN (not a number) values with .findna() and consider using .dropna() to clean up your DataFrame.

3. You can access entire columns of a DataFrame using the square bracket notation: df['column name'] or df[['column name 1', 'column name 2', 'column name 3']]

4. You can access individual cells in a DataFrame by chaining square brackets df['column name'][index] or using df['column name'].loc[index]

5. The largest and smallest values, as well as their positions, can be found with methods like .max(), .min(), .idxmax() and .idxmin()

6. You can sort the DataFrame with .sort_values() and add new columns with .insert()

7. To create an Excel Style Pivot Table by grouping entries that belong to a particular category use the .groupby() method


## Ipynb (Google Colaboratory) using pandas Day 2
**.pivot()**
Use this CSV as example:
[QueryResults.csv](https://github.com/EdmundLT/U-Python-100-Days/files/8247393/QueryResults.csv)

![image](https://user-images.githubusercontent.com/98913678/158230297-ff993a20-6097-40e9-948e-28e82005ce0a.png)
```
import pandas as pd
df = pd.read_csv("QueryResults.csv", names=['DATE', 'TAG', 'POSTS'], header=0)
df.DATE = pd.to_datetime(df.DATE)
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.head()
```
<img width="856" alt="image" src="https://user-images.githubusercontent.com/98913678/158231189-980c9da0-448b-4a8a-954d-8d77c70a2df2.png">

**Why there are "NaN Value"?**

use .isna() to find "NaN"

```
reshaped_df.fillna(0, inplace=True) 
```
<img width="868" alt="image" src="https://user-images.githubusercontent.com/98913678/158231500-906e7f99-2399-4ed9-a458-55235f6b909d.png">

## Metplotlib
To create our first charts we're going to use a library called Matplotlib. There are many different libraries in Python to help us create charts and graphs. Matplotlib is an incredibly popular one and it works beautifully in combination with Pandas, so let's check it out.

```
import matplotlib.pyplot as plt
```
**.plot()** https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
```
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("QueryResults.csv", names=['DATE', 'TAG', 'POSTS'], header=0)
df.DATE = pd.to_datetime(df.DATE)
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.fillna(0, inplace=True) 
plt.plot(reshaped_df.index, reshaped_df["java"])
```
<img width="393" alt="Screenshot 2022-03-14 at 1 54 44 PM" src="https://user-images.githubusercontent.com/98913678/158232203-45d39d10-be9a-422b-ac61-bead38dee261.png">

**Styling the Chart/Figure**

.figure() - allows us to resize our chart

.xticks() - configures our x-axis

.yticks() - configures our y-axis

.xlabel() - add text to the x-axis

.ylabel() - add text to the y-axis

.ylim() - allows us to set a lower and upper bound

```
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Num of Posts', fontsize=14)
plt.ylim(0, 35000)
plt.plot(reshaped_df.index, reshaped_df["java"])
```
<img width="866" alt="image" src="https://user-images.githubusercontent.com/98913678/158233603-12ded080-43b1-4510-80c2-20bd30ea4926.png">

**Multi line in 1 graph**
```
for col in reshaped_df.columns:
  plt.plot(reshaped_df.index, reshaped_df[col], linewidth=2, label=reshaped_df[col].name)
plt.legend(fontsize=16)
```
<img width="859" alt="Screenshot 2022-03-14 at 2 08 02 PM" src="https://user-images.githubusercontent.com/98913678/158234249-1be9faee-37df-49bd-96bb-916fa420ee6e.png">

**smooth line**
We can use .rolling() and .mean() method to make all lines smoother.
```
roll_df = reshaped_df.rolling(window=6).mean()
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Num of Posts', fontsize=14)
plt.ylim(0, 35000)
for col in roll_df.columns:
  plt.plot(roll_df.index, roll_df[col], linewidth=2, label=roll_df[col].name)
plt.legend(fontsize=16)
```
![image](https://user-images.githubusercontent.com/98913678/158234634-cbaa6611-514d-4593-b1e3-bd888e621c97.png)

## Summary for Day 2
Congratulations on completing another challenging data science project! Today we've seen how to grab some raw data and create some interesting charts using Pandas and Matplotlib. We've

1. used .groupby() to explore the number of posts and entries per programming language
2. converted strings to Datetime objects with to_datetime() for easier plotting
3. reshaped our DataFrame by converting categories to columns using .pivot()
4. used .count() and isna().values.any() to look for NaN values in our DataFrame, which we then replaced using .fillna()
5. created (multiple) line charts using .plot() with a for-loop
6. styled our charts by changing the size, the labels, and the upper and lower bounds of our axis.
7. added a legend to tell apart which line is which by colour
8. smoothed out our time-series observations with .rolling().mean() and plotted them to better identify trends over time.
