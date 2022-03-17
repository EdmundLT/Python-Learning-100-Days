## #This is all project from Day71 - Day80

Proeject List in order by Learning Day:

1. Ipynb (Google Colaboratory) using pandas
2. Google Trends Data Viz
3. Google Play Store Project
4. 

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

## Learning Points & Summary of Day 74
1. How to use .describe() to quickly see some descriptive statistics at a glance.
2. How to use .resample() to make a time-series data comparable to another by changing the periodicity.
3. How to work with matplotlib.dates Locators to better style a timeline (e.g., an axis on a chart).
4. How to find the number of NaN values with .isna().values.sum()
5. How to change the resolution of a chart using the figure's dpi
6. How to create dashed '--' and dotted '-.' lines using linestyles
7. How to use different kinds of markers (e.g., 'o' or '^') on charts.
8. Fine-tuning the styling of Matplotlib charts by using limits, labels, linewidth and colours (both in the form of named colours and HEX codes).
9. Using .grid() to help visually identify seasonality in a time series.


## Ipynb (Google Colaboratory) using pandas Day 75
```
.sample(n)
```
<img width="910" alt="Screenshot 2022-03-17 at 4 15 47 PM" src="https://user-images.githubusercontent.com/98913678/158887955-0156cf62-ab37-470a-8a2a-a61514a346d8.png">

**How to drop out some columns we dont need?**

```
.drop([column_1, column_2], axis = 1, inplace=T/F)
```
<img width="940" alt="Screenshot 2022-03-17 at 4 16 39 PM" src="https://user-images.githubusercontent.com/98913678/158888091-e138ab4e-08fb-4618-b5e8-0e159f6f028a.png">


**Any duplicate row?**
```
duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
print(duplicated_rows.shape)
duplicated_rows.head()
```

**.drop_duplicates() Method**
<img width="926" alt="Screenshot 2022-03-17 at 4 20 27 PM" src="https://user-images.githubusercontent.com/98913678/158888636-1a382670-292b-4fc1-a063-7b1a9ba39c38.png">

## Pie Graph

```import plotly.express as px```

parameters:
```
fig = px.pie(labels=ratings.index, values=ratings.values)
fig.show()
```
<img width="914" alt="Screenshot 2022-03-17 at 4 26 57 PM" src="https://user-images.githubusercontent.com/98913678/158889511-2ac8e08d-2041-441d-aa65-50fb491db880.png">

**Styling the Pie Graph**
```
fig = px.pie(labels=ratings.index,
values=ratings.values,
title="Content Rating",
names=ratings.index,
)
fig.update_traces(textposition='outside', textinfo='percent+label')
 
fig.show()
```
<img width="908" alt="Screenshot 2022-03-17 at 4 27 36 PM" src="https://user-images.githubusercontent.com/98913678/158889602-98183eb4-36ea-445a-9be5-78352ee10943.png">

Donut graph: add parameters - hole

<img width="926" alt="Screenshot 2022-03-17 at 4 29 20 PM" src="https://user-images.githubusercontent.com/98913678/158889832-7a586b73-fd6c-4311-93a9-660bfcd746f1.png">

## pd.to_numeric() Method
```
df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', '')
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
```
Before to_numeric:

<img width="611" alt="Screenshot 2022-03-17 at 4 35 02 PM" src="https://user-images.githubusercontent.com/98913678/158890634-c334eb5a-283c-4487-9649-e28e7cca0f5a.png">

After:
<img width="742" alt="Screenshot 2022-03-17 at 4 35 21 PM" src="https://user-images.githubusercontent.com/98913678/158890697-20c58b39-e244-4591-8de6-ee2d2ac3c0ed.png">

**Exercise**
1. Find how many Apps category?
<img width="358" alt="Screenshot 2022-03-17 at 4 40 28 PM" src="https://user-images.githubusercontent.com/98913678/158891519-a348fa22-d8e9-4303-9109-8e560fd3f28a.png">

2. Find top 10 category.
<img width="572" alt="Screenshot 2022-03-17 at 4 41 01 PM" src="https://user-images.githubusercontent.com/98913678/158891611-082eda9e-2941-4c0a-9b8f-bf6ab7c4a4bc.png">

3. plot a bar chart<img width="931" alt="Screenshot 2022-03-17 at 4 41 17 PM" src="https://user-images.githubusercontent.com/98913678/158891657-a8889edb-d29e-40b6-a83c-c2af11fbb414.png">
4. Another Aspect.
<img width="932" alt="Screenshot 2022-03-17 at 4 43 28 PM" src="https://user-images.githubusercontent.com/98913678/158892011-f92425a5-cf2e-4323-99ef-0af73881c848.png">

**Exercise 2**
First, we need to work out the number of apps in each category (similar to what we did previously).
<img width="768" alt="Screenshot 2022-03-17 at 4 44 10 PM" src="https://user-images.githubusercontent.com/98913678/158892112-de6f4100-120e-4d58-a3e2-6972d496df85.png">

Then we can use **.merge()** and combine the two DataFrames.

<img width="893" alt="Screenshot 2022-03-17 at 4 45 20 PM" src="https://user-images.githubusercontent.com/98913678/158892250-60a8946a-b2ee-4c4f-8d75-036db305f0c9.png">

Now we can create the chart. Note that we can pass in an entire DataFrame and specify which columns should be used for the x and y by column name.

<img width="923" alt="Screenshot 2022-03-17 at 4 46 35 PM" src="https://user-images.githubusercontent.com/98913678/158892390-5cec934c-f805-4607-ba11-1c476d0645e1.png">

**Exercise 3 - Comparing Free vs Paid**

Now that we’ve looked at the total number of apps per category and the total number of apps per genre, let’s see what the split is between free and paid apps.

```df_apps_clean.Type.value_counts()```
We see that the majority of apps are free on the Google Play Store. But perhaps some categories have more paid apps than others. Let’s investigate. We can group our data first by Category and then by Type. Then we can add up the number of apps per each type. Using as_index=False we push all the data into columns rather than end up with our Categories as the index.

<img width="930" alt="Screenshot 2022-03-17 at 4 48 46 PM" src="https://user-images.githubusercontent.com/98913678/158892669-4f600a59-48d6-4f27-8e1f-906308aa348b.png">

## Solution: Contrasting Free vs. Paid Apps per Category

<img width="913" alt="Screenshot 2022-03-17 at 4 51 51 PM" src="https://user-images.githubusercontent.com/98913678/158893064-511838ec-2aed-45ba-881c-60caa978382b.png">

##Solution: Create Box Plots for the Number of Installs

<img width="909" alt="Screenshot 2022-03-17 at 4 53 57 PM" src="https://user-images.githubusercontent.com/98913678/158893354-2aadfeae-bb7c-4f37-b096-d0860e328371.png">

## Solution: App Revenue by Category

<img width="910" alt="Screenshot 2022-03-17 at 4 55 21 PM" src="https://user-images.githubusercontent.com/98913678/158893560-ea777d40-16c9-49d2-b685-c0f6ad37ef4c.png">

## Solution: App Pricing by Category

First, we need to find the median price for an Android Apps.

<img width="335" alt="Screenshot 2022-03-17 at 4 56 44 PM" src="https://user-images.githubusercontent.com/98913678/158893784-762fbe5e-f447-4009-abbe-9b08e2e36a71.png">

However, some categories have higher median prices than others. This time we see that Medical apps have the most expensive apps as well as a median price of $5.49. In contrast, Personalisation apps are quite cheap on average at $1.49. Other categories which higher median prices are Business ($4.99) and Dating ($6.99). It seems like customers who shop in these categories are not so concerned about paying a bit extra for their apps.

<img width="914" alt="Screenshot 2022-03-17 at 4 57 44 PM" src="https://user-images.githubusercontent.com/98913678/158893944-be48e742-261c-4398-9e91-79b37db2b7bb.png">



