## Day 79 Dr Semmelweis Analysis

```
prob = df_yearly.deaths.sum() / df_yearly.births.sum() * 100
print(f'Chances of dying in the 1840s in Vienna: {prob:.3}%')
```

Chances of dying in the 1840s in Vienna: 7.08%

**Visualise the Total Number of Births 🤱 and Deaths 💀 over Time**

<img width="1142" alt="Screen Shot 2022-03-21 at 6 58 50 PM" src="https://user-images.githubusercontent.com/98913678/159376729-b0b58187-3583-40b4-8a64-145f7ed04928.png">

# Analysing the Yearly Data Split By Clinic

<img width="1145" alt="Screen Shot 2022-03-21 at 6 59 04 PM" src="https://user-images.githubusercontent.com/98913678/159376750-4668eebd-fbc9-450b-8e1d-108a3474986d.png">

<img width="1148" alt="Screen Shot 2022-03-21 at 6 59 17 PM" src="https://user-images.githubusercontent.com/98913678/159376771-855d4bb6-2a57-47a1-8906-7ffa7e822f2c.png">

```
df_yearly['pct_deaths'] = df_yearly.deaths / df_yearly.births * 100
```

```
clinic_1 = df_yearly[df_yearly.clinic == 'clinic 1']
avg_c1 = clinic_1.deaths.sum() / clinic_1.births.sum() * 100
avg_c2 = clinic_2.deaths.sum() / clinic_2.births.sum() * 100
print(f'Average death rate in clinic 1 is {avg_c1:.3}%.')
print(f'Average death rate in clinic 2 is {avg_c2:.3}%.')
```

Average death rate in clinic 1 is 9.92%.

Average death rate in clinic 2 is 3.88%.

<img width="1138" alt="Screen Shot 2022-03-21 at 6 59 53 PM" src="https://user-images.githubusercontent.com/98913678/159376821-4441400a-9740-49fa-ba4c-1d25ab8a3fde.png">

# The Effect of Handwashing

<img width="702" alt="Screen Shot 2022-03-21 at 7 00 08 PM" src="https://user-images.githubusercontent.com/98913678/159376853-01ed57f9-beac-46e8-85fd-ddee87fa1bc9.png">

<img width="618" alt="Screen Shot 2022-03-21 at 7 00 21 PM" src="https://user-images.githubusercontent.com/98913678/159376868-3ed7cb53-8685-4633-85c0-81bb0816c3ec.png">

![image](https://user-images.githubusercontent.com/98913678/159376872-53d32486-478a-48e5-83c6-78248d7c1f34.png)

# Visualising Distributions and Testing for Statistical Significance

```
avg_prob_before = before_washing.pct_deaths.mean() * 100
print(f'Chance of death during childbirth before handwashing: {avg_prob_before:.3}%.')
 
avg_prob_after = after_washing.pct_deaths.mean() * 100
print(f'Chance of death during childbirth AFTER handwashing: {avg_prob_after:.3}%.')
 
mean_diff = avg_prob_before - avg_prob_after
print(f'Handwashing reduced the monthly proportion of deaths by {mean_diff:.3}%!')
 
times = avg_prob_before / avg_prob_after
print(f'This is a {times:.2}x improvement!')
```

1. Chance of death during childbirth before handwashing: 10.5%.
2. Chance of death during childbirth AFTER handwashing: 5.07%.
3. Handwashing reduced the monthly proportion of deaths by 5.43%!

This is a 2.1x improvement!

<img width="1147" alt="Screen Shot 2022-03-21 at 7 01 05 PM" src="https://user-images.githubusercontent.com/98913678/159376937-7596ea20-508a-4a4f-9695-f16d6adc161d.png">

<img width="1144" alt="Screen Shot 2022-03-21 at 7 01 14 PM" src="https://user-images.githubusercontent.com/98913678/159376953-ee268521-01c4-4ed2-8e7e-99ee38d70c0a.png">

<img width="1146" alt="Screen Shot 2022-03-21 at 7 01 22 PM" src="https://user-images.githubusercontent.com/98913678/159376974-e6d7035d-ce33-4f5d-9625-948e2de96dfd.png">

<img width="1140" alt="Screen Shot 2022-03-21 at 7 01 30 PM" src="https://user-images.githubusercontent.com/98913678/159376988-b2d0a6c2-ae0d-4b27-9786-c2426b26ebd0.png">

<img width="593" alt="Screen Shot 2022-03-21 at 7 01 35 PM" src="https://user-images.githubusercontent.com/98913678/159376998-c844b684-6bdf-46cb-afb6-95ae45133272.png">

































