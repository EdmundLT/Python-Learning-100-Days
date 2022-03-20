## Ipynb (Google Colaboratory) using pandas Day 76

```
import pandas as pd
df = pd.read_csv("cost_revenue_dirty.csv", index_col="Rank")
df.sort_values("Rank", inplace=True)
```

### Check Datatype first!

<img width="1028" alt="Screen Shot 2022-03-20 at 3 09 36 PM" src="https://user-images.githubusercontent.com/98913678/159178638-6dde2384-e2f6-49c1-ba11-82331f6ac522.png">

<img width="1049" alt="Screen Shot 2022-03-20 at 3 10 14 PM" src="https://user-images.githubusercontent.com/98913678/159178663-6b4c3073-f6f9-4479-ac0f-22c131f2e779.png">

<img width="1072" alt="Screen Shot 2022-03-20 at 3 11 07 PM" src="https://user-images.githubusercontent.com/98913678/159178737-91e1bf9c-a4c4-4102-86a9-664b14f3cd83.png">

### Using the .query() function to filter on multiple conditions

<img width="1066" alt="Screen Shot 2022-03-20 at 3 11 36 PM" src="https://user-images.githubusercontent.com/98913678/159178754-ad335b78-bc0b-4f34-b908-05d99660b325.png">

## Removing the unreleased films

<img width="521" alt="Screen Shot 2022-03-20 at 3 12 27 PM" src="https://user-images.githubusercontent.com/98913678/159178809-bfbe4718-6922-4310-b29c-24d571549ef0.png">

### Budget greater than revenue

<img width="877" alt="Screen Shot 2022-03-20 at 3 12 46 PM" src="https://user-images.githubusercontent.com/98913678/159178821-877500fb-d16d-4a37-9a08-f8cc41cedc43.png">

37%!?

## Seaborn Data Visualisation: Bubble Charts

<img width="377" alt="Screen Shot 2022-03-20 at 3 13 07 PM" src="https://user-images.githubusercontent.com/98913678/159178827-3fbfaa5f-b940-4762-9560-a8f3a5e9c909.png">

![image](https://user-images.githubusercontent.com/98913678/159178833-0f57ccf6-972b-4551-ac92-b0caaba97a92.png)


### Styling the Charts

<img width="413" alt="Screen Shot 2022-03-20 at 3 13 21 PM" src="https://user-images.githubusercontent.com/98913678/159178841-cbd40242-4e01-4626-8151-89d7f1c82d69.png">

![image](https://user-images.githubusercontent.com/98913678/159178850-cc96101d-36bd-494e-ac9f-e5bd6dcceee3.png)


### From Scatter Plot to Bubble Chart****

<img width="534" alt="Screen Shot 2022-03-20 at 3 13 50 PM" src="https://user-images.githubusercontent.com/98913678/159178857-b97a9a18-8cb4-45ea-88e6-226c5a2fca55.png">

![image](https://user-images.githubusercontent.com/98913678/159178859-fb150417-b7da-4031-85b4-2dff99edbffd.png)

use darkgrid style

```
with sns.axes_style('darkgrid')
```

![image](https://user-images.githubusercontent.com/98913678/159178873-d0b16665-62c9-49d8-ba7b-b4a7f118de89.png)


<img width="685" alt="Screen Shot 2022-03-20 at 3 14 29 PM" src="https://user-images.githubusercontent.com/98913678/159178875-0cef1e3f-4f22-4b65-9948-e73493bd02fa.png">

![image](https://user-images.githubusercontent.com/98913678/159178880-ac7d11ff-f311-4b82-9d06-2972d7987a0d.png)


## Floor Division: A Trick to Convert Years to Decades

<img width="1135" alt="image" src="https://user-images.githubusercontent.com/98913678/159178903-2a8a466c-9216-47e7-aa06-865ebe88233b.png">

```
1991 // 10 = 199
199 * 10 = 1990
```


<img width="1019" alt="Screen Shot 2022-03-20 at 3 15 32 PM" src="https://user-images.githubusercontent.com/98913678/159178919-7b26f76b-2676-4c6a-a13b-e0cc014223b6.png">

<img width="1073" alt="Screen Shot 2022-03-20 at 3 15 40 PM" src="https://user-images.githubusercontent.com/98913678/159178925-4fbf624a-1267-4bf3-8f5a-03bf2b9987f3.png">


## Plotting Linear Regressions with Seaborn

```
sns.regplot(data=old_films, 
            x='USD_Production_Budget',
            y='USD_Worldwide_Gross')

```

![image](https://user-images.githubusercontent.com/98913678/159178942-9ee008ee-18a1-48b8-a538-5da1bd25568e.png)

### Styling

```
plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style("whitegrid"):
  sns.regplot(data=old_films, 
            x='USD_Production_Budget', 
            y='USD_Worldwide_Gross',
            scatter_kws = {'alpha': 0.4},
            line_kws = {'color': 'black'})
```

![image](https://user-images.githubusercontent.com/98913678/159178948-ad765335-ee73-41da-8a3b-057e16161595.png)

```
plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style("darkgrid"):
  sns.regplot(data=new_films, 
            x='USD_Production_Budget', 
            y='USD_Worldwide_Gross',
            scatter_kws = {'alpha': 0.4},
            line_kws = {'color': 'black'})
```

![image](https://user-images.githubusercontent.com/98913678/159178953-5ae9e39e-e9ac-4c90-8d7f-dffee0978200.png)


```
plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style('darkgrid'):
  ax = sns.regplot(data=new_films,
                   x='USD_Production_Budget',
                   y='USD_Worldwide_Gross',
                   color='#2f4b7c',
                   scatter_kws = {'alpha': 0.3},
                   line_kws = {'color': '#ff7c43'})
  
  ax.set(ylim=(0, 3000000000),
         xlim=(0, 450000000),
         ylabel='Revenue in $ billions',
         xlabel='Budget in $100 millions') 
```

![image](https://user-images.githubusercontent.com/98913678/159178959-97cf8043-6dd6-4b39-b041-e0891c2b417d.png)


## Use scikit-learn to Run Your Own Regression

![image](https://user-images.githubusercontent.com/98913678/159178966-9f669329-119e-4591-99ec-c52642b67d85.png)

To find the best possible line, our regression will estimate the y-intercept ("theta zero") and the slope ("theta one"). The line's intercept on the y-axis tells us how much revenue a movie would make if the budget was 0. The slope tells us how much extra revenue we get for a $1 increase in the movie budget.

![image](https://user-images.githubusercontent.com/98913678/159178970-0769a8fe-b408-40cc-a1f9-54692312439b.png)


## scikit-learn

<img width="950" alt="Screen Shot 2022-03-20 at 3 17 31 PM" src="https://user-images.githubusercontent.com/98913678/159178982-4eafd7e8-cdd8-4b2c-a581-847635af0fcd.png">


## Estimate a movie budget = 350000000

<img width="753" alt="Screen Shot 2022-03-20 at 3 17 46 PM" src="https://user-images.githubusercontent.com/98913678/159178990-8e46a193-e428-43d5-8420-743f6130c179.png">



# Summary

1. Use nested loops to remove unwanted characters from multiple columns

2. Filter Pandas DataFrames based on multiple conditions using both .loc[] and .query()

3. Create bubble charts using the Seaborn Library

4. Style Seaborn charts using the pre-built styles and by modifying Matplotlib parameters

5. Use floor division (i.e., integer division) to convert years to decades

6. Use Seaborn to superimpose a linear regressions over our data

7. Make a judgement if our regression is good or bad based on how well the model fits our data and the r-squared metric

8. Run regressions with scikit-learn and calculate the coefficients.












