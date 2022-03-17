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
