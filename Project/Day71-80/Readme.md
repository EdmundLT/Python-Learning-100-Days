## #This is all project from Day71 - Day80

Proeject List in order by Learning Day:

1.

## Concepts Used in Day71 - Day80

## Ipynb (Google Colaboratory)

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

```
## Summary
1. Use .head(), .tail(), .shape and .columns to explore your DataFrame and find out the number of rows and columns as well as the column names.

2. Look for NaN (not a number) values with .findna() and consider using .dropna() to clean up your DataFrame.

3. You can access entire columns of a DataFrame using the square bracket notation: df['column name'] or df[['column name 1', 'column name 2', 'column name 3']]

4. You can access individual cells in a DataFrame by chaining square brackets df['column name'][index] or using df['column name'].loc[index]

5. The largest and smallest values, as well as their positions, can be found with methods like .max(), .min(), .idxmax() and .idxmin()

6. You can sort the DataFrame with .sort_values() and add new columns with .insert()

7. To create an Excel Style Pivot Table by grouping entries that belong to a particular category use the .groupby() method
```
