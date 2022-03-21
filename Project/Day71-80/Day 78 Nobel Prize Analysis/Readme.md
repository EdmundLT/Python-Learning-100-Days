## Day 78 Nobel Prize Analysis

```
import pandas as pd

df = pd.read_csv("nobel_prize_data.csv", )

df.head(5)
```

**Creating a Donut Chart with Plotly**

```
biology = df.sex.value_counts()
```

```
fig = px.pie(labels=biology.index,
values=biology.values,
title="Percentage of Male vs. Female Winner",
names=biology.index,
hole=0.6
)
fig.update_traces(textposition='outside', textinfo='percent+label')
 
fig.show()
```

<img width="1082" alt="Screen Shot 2022-03-20 at 11 51 37 PM" src="https://user-images.githubusercontent.com/98913678/159203089-7aa3e541-5fdd-4fe8-ba17-ed9012688506.png">

**The first 3 women to win**

<img width="728" alt="Screen Shot 2022-03-20 at 11 52 09 PM" src="https://user-images.githubusercontent.com/98913678/159203127-cbd696ad-f171-4db5-89e5-140c79d5a715.png">

**The Repeat Winners**

<img width="727" alt="Screen Shot 2022-03-20 at 11 52 28 PM" src="https://user-images.githubusercontent.com/98913678/159203149-ed9a9949-d116-4956-b0c6-d68b22629407.png">

**Number of Prizes per Category**

<img width="1140" alt="Screen Shot 2022-03-20 at 11 52 46 PM" src="https://user-images.githubusercontent.com/98913678/159203173-0f078670-8162-4876-a55f-2aa69a7103ec.png">

**The Economics Prize**

<img width="1151" alt="Screen Shot 2022-03-20 at 11 53 16 PM" src="https://user-images.githubusercontent.com/98913678/159203204-50d7eb8d-7378-4b73-9627-169384fad267.png">

**Male and Female Winners by Category**

<img width="728" alt="Screen Shot 2022-03-20 at 11 53 43 PM" src="https://user-images.githubusercontent.com/98913678/159203226-f3eac82e-f931-409d-ba3a-79c73774b925.png">

<img width="1141" alt="Screen Shot 2022-03-20 at 11 53 54 PM" src="https://user-images.githubusercontent.com/98913678/159203239-a782a17b-0020-4a73-8c73-2de14ffcf2fa.png">

**Number of Prizes Awarded over Time**

<img width="896" alt="Screen Shot 2022-03-20 at 11 54 11 PM" src="https://user-images.githubusercontent.com/98913678/159203257-958142ae-0d83-457c-9df0-1123c59f906e.png">

**Generate year timeline Using Numpy**

```
np.arange(1900, 2021, step=5)
```

<img width="1133" alt="Screen Shot 2022-03-20 at 11 54 41 PM" src="https://user-images.githubusercontent.com/98913678/159203285-ce7e0ace-8d19-48b1-9507-d2da69029433.png">

**The Prize Share of Laureates over Time**

<img width="744" alt="Screen Shot 2022-03-20 at 11 55 01 PM" src="https://user-images.githubusercontent.com/98913678/159203309-a6569fdd-b4dd-4223-bb34-e1aaf4b64086.png">

<img width="1136" alt="image" src="https://user-images.githubusercontent.com/98913678/159203355-d99d5d8e-38e4-4c6b-8c7d-2eb571257435.png">

# A Choropleth Map and the Countries with the Most Prizes

**Prize ranking by Country**

<img width="755" alt="Screen Shot 2022-03-20 at 11 57 29 PM" src="https://user-images.githubusercontent.com/98913678/159203477-931a0925-e496-4837-b170-ce5c5ea3a275.png">

<img width="1144" alt="Screen Shot 2022-03-20 at 11 57 37 PM" src="https://user-images.githubusercontent.com/98913678/159203483-1799f10e-ab03-4460-b5c7-1ce3850ee07c.png">

**Displaying the Data on a Map**

<img width="777" alt="Screen Shot 2022-03-20 at 11 58 35 PM" src="https://user-images.githubusercontent.com/98913678/159203549-eb4a76ab-aaad-483f-bdbe-fa32d7fc4b62.png">

<img width="1155" alt="Screen Shot 2022-03-20 at 11 58 59 PM" src="https://user-images.githubusercontent.com/98913678/159203568-1b0663ed-306b-4efa-aa55-3ac82f71a9a2.png">

**Displaying the Data on a Map**

<img width="812" alt="Screen Shot 2022-03-20 at 11 59 27 PM" src="https://user-images.githubusercontent.com/98913678/159203591-7c50b05b-31fe-439b-8ca8-ffa2a0a94051.png">

<img width="1143" alt="Screen Shot 2022-03-20 at 11 59 46 PM" src="https://user-images.githubusercontent.com/98913678/159203608-739922a2-75ff-41e8-adc0-e7a8fd1c3122.png">

**Country Prizes over Time**

<img width="872" alt="Screen Shot 2022-03-20 at 11 59 59 PM" src="https://user-images.githubusercontent.com/98913678/159203620-f39e9c6b-187d-4299-a3a0-abf4a29543d5.png">

<img width="1146" alt="Screen Shot 2022-03-21 at 12 00 09 AM" src="https://user-images.githubusercontent.com/98913678/159203639-beae975e-42e6-4323-8470-fa19f3c5d183.png">

# Create Sunburst Charts for a Detailed Regional Breakdown of Research Locations

**Create a bar chart showing the organisations affiliated with the Nobel laureates**

<img width="764" alt="Screen Shot 2022-03-21 at 12 02 53 AM" src="https://user-images.githubusercontent.com/98913678/159203813-36ee0f17-1d3d-49b5-83cd-24715a93883b.png">

<img width="1154" alt="Screen Shot 2022-03-21 at 12 03 02 AM" src="https://user-images.githubusercontent.com/98913678/159203825-e90c7e4c-b74a-4c9e-9c8f-0602d7547211.png">

**Create another plotly bar chart graphing the top 20 organisation cities of the research institutions associated with a Nobel laureate.**

<img width="748" alt="Screen Shot 2022-03-21 at 12 03 18 AM" src="https://user-images.githubusercontent.com/98913678/159203843-97200d15-a610-4ef6-8bbe-3f2768b48fbc.png">

<img width="1143" alt="Screen Shot 2022-03-21 at 12 03 27 AM" src="https://user-images.githubusercontent.com/98913678/159203852-43948276-f851-4909-ba3a-8c98e216964d.png">

**Laureate Birth Cities**

<img width="1149" alt="Screen Shot 2022-03-21 at 12 03 40 AM" src="https://user-images.githubusercontent.com/98913678/159203865-2ea3450d-2ac8-4f12-960a-c5b1b7154473.png">

**The Sunburst Chart**

<img width="1000" alt="Screen Shot 2022-03-21 at 12 03 54 AM" src="https://user-images.githubusercontent.com/98913678/159203878-323e04c8-adab-4da6-896d-0f83e928c395.png">

<img width="1144" alt="Screen Shot 2022-03-21 at 12 04 00 AM" src="https://user-images.githubusercontent.com/98913678/159203886-c4f64dcb-97d2-4ab4-82e9-e3472393e582.png">

# Unearthing Patterns in the Laureate Age at the Time of the Award

<img width="1156" alt="Screen Shot 2022-03-21 at 12 04 17 AM" src="https://user-images.githubusercontent.com/98913678/159203901-8eff1957-2db0-486c-92fe-5df2a1503586.png">

**Descriptive Statistics and Histogram**

<img width="1154" alt="Screen Shot 2022-03-21 at 12 04 41 AM" src="https://user-images.githubusercontent.com/98913678/159203940-bb64941b-f4f4-4c8d-a416-829664cd6887.png">

**Winning Age Over Time (All Categories)**

<img width="1163" alt="Screen Shot 2022-03-21 at 12 04 56 AM" src="https://user-images.githubusercontent.com/98913678/159203962-c91da811-426a-4a37-a0a5-1d3a46f73396.png">

**Age Differences between Categories**

<img width="1145" alt="Screen Shot 2022-03-21 at 12 05 08 AM" src="https://user-images.githubusercontent.com/98913678/159203976-cb2b4c8a-e20d-45d3-aa81-f68df96ca6a5.png">

**Laureate Age over Time by Category**

<img width="482" alt="Screen Shot 2022-03-21 at 12 05 23 AM" src="https://user-images.githubusercontent.com/98913678/159203999-6251fb9b-2b23-44b8-b30d-145215d1a85c.png">

![image](https://user-images.githubusercontent.com/98913678/159204006-a22aceb5-7819-4af7-99e7-699f6bb37ef8.png)

<img width="890" alt="Screen Shot 2022-03-21 at 12 05 38 AM" src="https://user-images.githubusercontent.com/98913678/159204019-5cc2ac49-5bd2-48b7-9f97-b9922baef279.png">






















