## Ipynb (Google Colaboratory) using pandas Day 76

Completed Ipynb file are available to download.

## Dimension
```
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from PIL import Image
```
**1-Dimension**

<img width="454" alt="Screen Shot 2022-03-19 at 3 04 38 PM" src="https://user-images.githubusercontent.com/98913678/159135001-c84557e7-f20a-4438-af8b-f32356e30a28.png">

<img width="710" alt="Screen Shot 2022-03-19 at 3 04 49 PM" src="https://user-images.githubusercontent.com/98913678/159135003-2bb94785-9e8a-484e-b4de-76ff21baae2c.png">

<img width="554" alt="Screen Shot 2022-03-19 at 3 05 05 PM" src="https://user-images.githubusercontent.com/98913678/159135012-3d8dde68-fcff-489e-bb35-f33cf7833b52.png">


To access the value 18 we, therefore, have to provide three different indices - one for each axis. As such, we locate the number at index 2 for the first axis, index number 1 for the second axis, and index number 3 for the third axis.

<img width="1158" alt="Screen Shot 2022-03-19 at 3 05 36 PM" src="https://user-images.githubusercontent.com/98913678/159135029-76bd6ce3-ff3b-4bc1-bbd3-a745dd644f64.png">

<img width="568" alt="Screen Shot 2022-03-19 at 3 06 03 PM" src="https://user-images.githubusercontent.com/98913678/159135039-af514b51-1469-4f34-a2e4-ea1180b66333.png">

## **Broadcasting, Scalars and Matrix Multiplication**

<img width="346" alt="Screen Shot 2022-03-19 at 3 06 39 PM" src="https://user-images.githubusercontent.com/98913678/159135055-8499b4c9-ee63-4b92-af0c-39cf4a1ce924.png">

![2020-10-12_16-01-36-b9c2fefd91ad6764599526cd883cc721](https://user-images.githubusercontent.com/98913678/159135063-883f96d3-07ac-4771-b8c2-60967e58cd26.gif)

<img width="400" alt="Screen Shot 2022-03-19 at 3 07 16 PM" src="https://user-images.githubusercontent.com/98913678/159135074-318783f1-638d-4cc3-8511-562858cb93af.png">

## Manipulating Images as ndarrays


<img width="498" alt="Screen Shot 2022-03-19 at 3 08 16 PM" src="https://user-images.githubusercontent.com/98913678/159135107-506e099e-cf85-4790-a208-4558f52ff1d2.png">


**Converting an image to grayscale**

```
sRGB_array = img / 255
```

**use matrix multiplication to multiply our two ndarrays together.**

```
grey_vals = np.array([0.2126, 0.7152, 0.0722])
```

**the values given by the formula above**

<img width="483" alt="Screen Shot 2022-03-19 at 3 09 13 PM" src="https://user-images.githubusercontent.com/98913678/159135134-990d26f1-987b-45e2-8c90-fd4c50459e37.png">

**Rotate image**

<img width="1057" alt="Screen Shot 2022-03-19 at 3 09 53 PM" src="https://user-images.githubusercontent.com/98913678/159135151-6a26d90d-0a54-4748-822c-3fcf8afe0329.png">

<img width="496" alt="Screen Shot 2022-03-19 at 3 10 03 PM" src="https://user-images.githubusercontent.com/98913678/159135155-8344ce24-816e-48ad-a92a-8d6d4c9489c9.png">




















In this lesson we looked at how to:

1. Create arrays manually with np.array()
2. Generate arrays using  .arange(), .random(), and .linspace()
3. Analyse the shape and dimensions of a ndarray
4. Slice and subset a ndarray based on its indices
5. Do linear algebra like operations with scalars and matrix multiplication
6. Use NumPys broadcasting to make ndarray shapes compatible
7. Manipulate images in the form of ndarrays

