## #This is all project from Day71 - Day80

Proeject List in order by Learning Day:

1.

## Concepts Used in Day71 - Day80

## Ipynb (Google Colaboratory) using pandas Day 71

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


## Summary of Day 71
1. Use .head(), .tail(), .shape and .columns to explore your DataFrame and find out the number of rows and columns as well as the column names.

2. Look for NaN (not a number) values with .findna() and consider using .dropna() to clean up your DataFrame.

3. You can access entire columns of a DataFrame using the square bracket notation: df['column name'] or df[['column name 1', 'column name 2', 'column name 3']]

4. You can access individual cells in a DataFrame by chaining square brackets df['column name'][index] or using df['column name'].loc[index]

5. The largest and smallest values, as well as their positions, can be found with methods like .max(), .min(), .idxmax() and .idxmin()

6. You can sort the DataFrame with .sort_values() and add new columns with .insert()

7. To create an Excel Style Pivot Table by grouping entries that belong to a particular category use the .groupby() method


## Ipynb (Google Colaboratory) using pandas Day 72
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

## Summary for Day 72
Congratulations on completing another challenging data science project! Today we've seen how to grab some raw data and create some interesting charts using Pandas and Matplotlib. We've

1. used .groupby() to explore the number of posts and entries per programming language
2. converted strings to Datetime objects with to_datetime() for easier plotting
3. reshaped our DataFrame by converting categories to columns using .pivot()
4. used .count() and isna().values.any() to look for NaN values in our DataFrame, which we then replaced using .fillna()
5. created (multiple) line charts using .plot() with a for-loop
6. styled our charts by changing the size, the labels, and the upper and lower bounds of our axis.
7. added a legend to tell apart which line is which by colour
8. smoothed out our time-series observations with .rolling().mean() and plotted them to better identify trends over time.


## Ipynb (Google Colaboratory) using pandas Day 73

Data:
[LEGO+Notebook+and+Data+(start).zip](https://github.com/EdmundLT/U-Python-100-Days/files/8247623/LEGO%2BNotebook%2Band%2BData%2B.start.zip)

**.nunique()**
DOC: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nunique.html?highlight=nunique#pandas.DataFrame.nunique

Count number of distinct elements in specified axis
```
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/colors.csv")
df['name'].nunique()
```
find how many colors are "is_trans"



Method 1:
```
df.groupby('is_trans').count()
```
<img width="308" alt="Screenshot 2022-03-14 at 2 25 34 PM" src="https://user-images.githubusercontent.com/98913678/158236975-71fcf16b-bb88-4b1b-84af-f05b3a8e7485.png">

Method 2:
**.value_counts()**
```
df.is_trans.value_counts()
```
<img width="260" alt="Screenshot 2022-03-14 at 2 28 31 PM" src="https://user-images.githubusercontent.com/98913678/158237476-dacf06a7-3e88-4389-a3a6-d8b90c977b6a.png">

## Lego Sets
```
sets_by_year = df.groupby('year').count()
sets_by_year['set_num'].head()
sets_by_year['set_num'].tail()
plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
```
![image](https://user-images.githubusercontent.com/98913678/158239063-f3159553-d73f-423e-954b-5e72d66bb646.png)

**.agg()**
![image](https://user-images.githubusercontent.com/98913678/158239354-7eb19a10-28d9-43e7-9653-25a2918c4317.png)

.agg() take **Dictionary** as an argument.

**Create a line plot of the number of themes released year-on-year. Only include the full calendar years in the dataset (1949 to 2019).**

```
themes_by_year = df.groupby('year').agg({'theme_id': pd.Series.nunique})
themes_by_year.rename(columns = {'theme_id': 'nr_themes'}, inplace = True)
plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
```
![image](https://user-images.githubusercontent.com/98913678/158240146-7f5ac777-9fba-415d-a08b-74bed5826c12.png)

**Combined graph**
![image](https://user-images.githubusercontent.com/98913678/158240495-f0962e3b-1cc7-4a55-9c35-c59932a6fd66.png)

sets by year are 0 - 90, but themes by year are from 0 - 900, how to balance it, make the graph easier to read?
```
ax1 = plt.gca() # get current axes
ax2 = ax1.twinx() <- share same x axis using .twinx()

ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])

#Styling
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Sets', color='red')
ax2.set_ylabel('Number of Themes', color='green')
```
![image](https://user-images.githubusercontent.com/98913678/158241255-66034b50-93b8-43de-9747-e4d0cc07a7ca.png)

**.scatter()**
```
parts_per_set = df.groupby('year').agg({'num_parts': pd.Series.mean})
plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
```
![image](https://user-images.githubusercontent.com/98913678/158242213-b8e43dba-c675-441b-9501-20abcdda17d0.png)

**Number of Sets per LEGO Theme**
![image](https://user-images.githubusercontent.com/98913678/158242489-36bf07be-2f5b-4018-9043-aeaad4661bac.png)

## database schema
![image](https://user-images.githubusercontent.com/98913678/158243251-efc497e4-40fe-4673-8864-427fe0e14478.png)
Search theme name "Star Wars"
```
themes = pd.read_csv('data/themes.csv')
themes[themes.name == 'Star Wars']
```
<img width="257" alt="Screenshot 2022-03-14 at 3 07 03 PM" src="https://user-images.githubusercontent.com/98913678/158243348-8299feac-5bd0-45ef-86e4-abc8ac1b8c0a.png">

**.merge()**
```
themes = pd.read_csv('data/themes.csv')
sets = pd.read_csv("data/sets.csv")
themes[themes.name == 'Star Wars']
set_theme_count = df["theme_id"].value_counts()
set_theme_count[:5]
set_theme_count = pd.DataFrame({'id' :set_theme_count.index,
                                'set_count' :set_theme_count.values})
merged_df = pd.merge(set_theme_count, themes, on='id')

#Styling
plt.figure(figsize=(14, 8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.bar(merged_df.name[:10], merged_df.set_count[:10])
```
![image](https://user-images.githubusercontent.com/98913678/158245306-a8f822c4-01d9-4fa1-8c5e-d029efdd6275.png)

## Learning Points & Summary of Day 73
In this lesson we looked at how to:

use HTML Markdown in Notebooks, such as section headings # and how to embed images with the <img> tag.

combine the groupby() and count() functions to aggregate data

use the .value_counts() function

slice DataFrames using the square bracket notation e.g., df[:-2] or df[:10]

use the .agg() function to run an operation on a particular column

rename() columns of DataFrames

create a line chart with two separate axes to visualise data that have different scales.

create a scatter plot in Matplotlib

work with tables in a relational database by using primary and foreign keys

.merge() DataFrames along a particular column

create a bar chart with Matplotlib

