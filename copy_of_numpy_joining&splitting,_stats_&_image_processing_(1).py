# -*- coding: utf-8 -*-
"""Copy of NumPy- Joining&Splitting, Stats & Image Processing (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19yCmJgK_HIu3XizzOEl11_iua8YWYx4z

## NumPy in Depth

### <font color=pink>Recap of Past Concepts: NumPy Arrays</font>
"""

#Import numpy library

#Create list in Python

#Convert list to NumPy array

#display the NumPy array

"""### Today's topic:: Splitting NumPy Arrays, but before splitting let's see how to join NumPy Arrays

#### <font color=violet>Joining NumPy Arrays</font>

Joining means putting contents of two or more arrays in a single array.

In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.

We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.

Syntax:

np.concatenate((array1,array2),axis=0) axis=0(along columns), axis=1(along rows)
"""

#concatenate two 1 D arrays
import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[4,5],[6,7]])
arr=np.concatenate((arr1,arr2))
arr
# 2D array
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[4,5],[6,7]])
arr=np.concatenate((arr1,arr2),axis=1)
arr


#2Darray
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[4,5],[6,7]])
arr=np.concatenate((arr1,arr2),axis=0)
arr


a=np.array([[1,2],
           [3,4]])
b=np.array([[5,6]])
np.concatenate((a,b),axis=0)
#2Darray
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[4,5],[6,7]])
arr=np.concatenate((arr1,arr2),axis=0)
arr


a=np.array([[1,2],
           [3,4]])
b=np.array([[5,6]])
np.concatenate((a,b),axis=0)

np.concatenate((a,b.T),axis=1)

"""#### <font color=red>Exercise: Join 2 2D arrays using any example of your choice</font>"""

a=np.array([[1,2],
           [3,4]])
b=np.array([[5,6]])
np.concatenate((a,b),axis=0)

np.concatenate((a,b.T),axis=1)

"""### Stack Functions

Joining Arrays Using Stack Functions
Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.

We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.
"""

# using stack function
#dimensions =1+ given dimensions 
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.stack((arr1,arr2),axis=1)
arr

arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[7,8,9],[10,11,12]])
arr=np.stack((arr1,arr2),axis=1)
arr

"""Stacking Along Rows
NumPy provides a helper function: hstack() to stack along rows.

#### <font color=red>Exercise: Join 2 2D arrays using hstack. Hint:hstack has no axis parameter</font>
"""

#dimensions same

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.hstack((arr1,arr2))
arr

arr1=np.array([[1,2,3],
               [4,5,6]])
arr2=np.array([[7,8,9],
              [10,11,12]])
arr=np.hstack((arr1,arr2))
#similar to concatenate (axis=1)
arr

"""Stacking Along Columns
NumPy provides a helper function: vstack() to stack along columns

#### <font color=red>Exercise: Join 2 2D arrays using vstack</font>
"""

#dimensions not same

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.vstack((arr1,arr2))
arr

#dimensions ramains same

arr1=np.array([[1,2,3],
               [4,5,6]])
arr2=np.array([[7,8,9],
              [10,11,12]])
arr=np.vstack((arr1,arr2))
#similar to concatenate (axis=1)
arr

"""## Splitting NumPy Arrays

Splitting is reverse operation of Joining.

Joining merges multiple arrays into one and Splitting breaks one array into multiple.

We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
"""

#Splitting array
arr=np.array([1,2,3,4,5,6])
new_arr=np.array_split(arr,3)
new_arr

#Slicing array
arr=np.array([1,2,3,4,5,6])
arr[1:5]

"""#### <font color=red>Split the array in 4 parts:</font>"""

arr=np.array([1,2,3,4,5,6,7])
new_arr=np.array_split(arr,4)
new_arr

"""The return value of the array_split() method is an array containing each of the split as an array.

If you split an array into 3 arrays, you can access them from the result just like any array element:

Example
"""

#splitting arrays and accessing them by indexes

arr=np.array([1,2,3,4,5,6])
new_arr=np.array_split(arr,3)
new_arr[0]

"""Splitting 2-D Arrays
Use the same syntax when splitting 2-D arrays.

Use the array_split() method, pass in the array you want to split and the number of splits you want to do.
"""

#splitting a 2D array
arr=np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
np.array_split(arr,3)

"""## Homework- Imp for Interviews: Read and revise about Indexing, Slicing, Join, Split, Search & Sort: Contact me for important links, docs for studying

### <font color=blue>Statistics in NumPy</font>

Go through official documentation:
https://numpy.org/doc/stable/reference/routines.statistics.html
"""

# pick up anything-- lets pick up percentile





"""[link text](https:// [link text](https://))### Random Numbers in NumPy

Random number does NOT mean a different number every time. Random means something that can not be predicted logically.
"""

#random integer less than 100
from numpy import random
random.randint(100)

#random float from 0 to 1
random.rand()

#float(random.randrange(155, 389))

# generating 5 random integers for 1 D array from 0 to 100
x=random.randint(100,size=(5))
x

# generating 3X5 random integers for 2 D array from 0 to 100
x=random.randint(100,size=(3,5))
x

"""Randomness has very important applications in many areas of mathematics. In statistics, the selection of a random sample is important to ensure that a study is conducted without bias. A simple random sample is obtained by numbering every member of the population of interest, and assigning each member a numerical label.

### Normal Distribution

The Normal Distribution is one of the most important distributions.

It is also called the Gaussian Distribution

It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.

Use the random.normal() method to get a Normal Data Distribution.

It has three parameters:

loc - (Mean) where the peak of the bell exists.

scale - (Standard Deviation) how flat the graph distribution should be.

size - The shape of the returned array.
"""

random.normal()

#random-normal distribution in a 2*3 array
random.normal(size=(2,3))

"""#### <font color=red>Exercise:Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2</font>"""

#normal distribution-visualization
random.normal(size=(2,3),loc=1,scale=2)

import seaborn as sns
#import matplotlib.pyplot as plt
sns.distplot(random.normal(size=(2,3),loc=1,scale=2),hist=False)

"""For a normal distribution, 68% of the observations are within +/- one standard deviation of the mean, 95% are within +/- two standard deviations, and 99.7% are within +- three standard deviations.

## Homework- Imp for Interviews: Read and revise about NumPy common statistics functions like mean, median, mode, percentiles, quintiles
## Also learn & revise the theory behind Normal/Gaussian Distribution, Binomial Distribution & Poisson distribution.
## Popular Question: What do you mean by Central Limit Theorem?

## <font color=green>Image Processing in NumPy</font>
"""

# importing all the required libraries
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

"""Pillow package is one of the important libraries of python for image manipulation. Pillow is a free and open source library for the Python programming language that allows you to easily create & manipulate digital images

PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities. the ImageOps module contains a number of 'ready-made' image processing operations. This module is somewhat experimental, and most operators only work on L and RGB images
"""

#open image

#attributes

#Rotate image by 90 degree

"""Negative of an Image
Converting a color image to a negative image is very simple. You to perform only 3 steps for each pixel of the image

First, get the RGB values of the pixel
Calculate new RGB values using R = 255 ??? R, G = 255 ??? G, B = 255- B
Finally, save the new RGB values in the pixel
Check the below code to convert an image to a negative image.
"""

#Negative of grey image

"""### Try doing something new to the image: making it black & white/ completely blue/ changing background color/color reduction/360 degree rotation etc

## <font color=red> Once mastered, go to Kaggle.com for Image processing projects using NumPy & SciPy</font>
"""