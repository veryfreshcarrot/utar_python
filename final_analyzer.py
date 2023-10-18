from collections import Counter
import re
from nltk.stem import PorterStemmer

# Given text
text = """
UNIVERSITI TUNKU ABDUL RAHMAN
ACADEMIC YEAR 2018/2019
SEPTEMBER EXAMINATION
UEMH4333 MACHINE VISION
THURSDAY, 20 SEPTEMBER 2018 TIME : 9.00 AM — 11.00 AM (2 HOURS)
BACHELOR OF ENGINEERING (HONS) MECHATRONICS ENGINEERING
Instructions to Candidates :
This question paper consists of FIVE (5) questions.
Each question carries 25 marks.
Answer ALL THREE (3) questions from Section-A, and ANY ONE (1) question from
Section-B.

This question paper consists of 5 questions on 4 printed pages.
UEMH4333 MACHINE VISION
Section-A [Answer ALL THREE (3) questions]
Ql.
Q2.
(a)
(b)
(c)
(a)
Explain briefly the THREE (3) key components of Machine Vision System.
(3 marks)
Machine vision methods can generally divided into image enhancement and
image analysis.
(1) Explain about image enhancement and image analysis. (4 marks)
(ii) | Give TWO (2) methods from each group in (i) and elaborate on the
methods in detail with examples. (12 marks)
Machine vision can be performed at various levels. The most complex level is
the object level, where meaningful properties such as size and shape can be
computed. Describe THREE (3) levels of computation with one example
each. (6 marks)
[Total : 25 marks]
Models of a step, ramp and roof edge, and their corresponding intensity profiles,
are shown in Figure 2.1.
| :
 
Figure 2.1
(1) Suppose that we compute gradient magnitude of each of these models
using Prewitt operators in Figure 2.2. Sketch the respective gradient
image and horizontal profile of these models through the center of each
gradient image. (6 marks)
an - r | a
am ‘aa
ts
iH @ 4
sc GRUNER na ORS SNEED
ay ‘ome
sar
omen ‘
| Pcncocinacnom aaa ERT KRRAICD er eRES TR
i <a, om
psn Shaan Poaccorcc Ror eevee
ome
‘neces
lereenerecenemantcrnesthercmimeneuntcsecmnbboneencwonsiommenet
es NA
isi hcg abit i :
Figure 2.2
(ii) | Sketch a horizontal profile for each corresponding angle image. Explain

your result. (8 marks)
This question paper consists of 5 questions on 4 printed pages.
UEMH4333 MACHINE VISION
Q2. (Continued)
Q3.
(b)
(c)
(a)
(b)
Chain codes are used to describe the contours of an image object. It is robust
against rotation. For this question, use top left point as the starting location and
follow anti-clockwise direction when calculating the difference code. For the
object in Figure 2.3, derive the chain code, the difference code, and the
normalized shape number.
 Figure 2.3
(6 marks)
A contour may be represented as an ordered list of edges or by a curve. A curve
is a mathematical model for a contour. There are several criteria for a good
contour representation. Briefly explain them. (5 marks)
[Total : 25 marks]
(i) Describe the main steps in the application of Hough transform in order
to locate objects in digital images. (4 marks)
(ii) State TWO (2) advantages offered by Hough transform based on
Q3(a)(i). Explain why these advantages arise. (4 marks)
Hamming Distance is a fast and effective method to determine similarity.
(i) Define the Hamming Distance between two binary images with
numerical example. (4 marks)
(ii) | Your group mate has proposed the use of the Hamming Distance for
measuring the similarity of two 8-bit grayscale images. He proposes to
apply the Hamming Distance directly such that the distance between
intensity 118 and intensity 120 is 1. Explain whether this method is

workable. (5 marks)
This question paper consists of 5 questions on 4 printed pages.
UEMH4333 MACHINE VISION
Q3(b). (Continued)
(iii) In iris recognition, the feature is extracted from a circular template.
Assuming that the extracted iris features are all in binary form. Head
orientation will cause rotation effect on the binary features. If Hamming
Distance is being applied for matching purpose, suggest a solution to
mitigate this problem. Explain with numerical example. (8 marks)

[Total : 25 marks]
Section-B [Answer ANY ONE (1) question]
Q4.
Q35.
(a)
(b)
(c)
(a)
(b)
Explain the differences between fixed threshold, ranged threshold, and general
threshold methods. (6 marks)
Construct and explain a morphological algorithm for converting an 8-connected
boundary to an m-connected boundary. You may assume that the boundary is
fully connected with thickness of one pixel. (14 marks)
Define the term “convolution”. Explain the application of convolution in image
processing. (5 marks)
[Total : 25 marks]
(i) The median, ¢, of a set of numbers is such that half the values in the set
are below ¢ while the other half are above it. For instance, the median of
the set of values {2,3,8,20,21,25,31} is 20. Show that an operator that
computes the median of a subimage area, S, is nonlinear. (8 marks)
(ii) Develop a formulation for computing the median of an nxn
neighborhood. (5 marks)
(iii) | Propose and explain a technique to update the pixel value as the center
of the neighborhood mentioned in Q5(a)(ii) is moving from pixel to pixel
within an image. (5 marks)
(1) Explain the differences between Mean filtering and Gaussian filtering.
(4 marks)
(ii) | Discuss briefly about the mask designs and the blurring effect caused by
Mean filtering and Gaussian filtering. (3 marks)

[Total : 25 marks]
This question paper consists of 5 questions on 4 printed pages.
UNIVERSITI TUNKU ABDUL RAHMAN
ACADEMIC YEAR 2019/2020
SEPTEMBER EXAMINATION
UEMH4333 MACHINE VISION
THURSDAY, 19 SEPTEMBER 2019 TIME : 2.00 PM — 4.00 PM (2 HOURS)
BACHELOR OF ENGINEERING (HONOURS) MECHATRONICS ENGINEERING
Instructions to Candidates :
This question paper consists of FIVE (5) questions.
Each question carries 25 marks.
Answer ALL THREE (3) questions from Section-A, and ANY ONE (1) question from
Section-B.
 This question paper consists of 5 questions on 5 printed pages.
UEMH4333 MACHINE VISION
Section-A (Answer ALL THREE (3) questions.)
Ql. (a)
(b) o~ QO Ne
(d)
(e)
Explain the FOUR (4) main characteristic of Machine V ision System. Vv y
(4 marks)
Give FOUR (4) nasty realities which are faced by machine vision algorithms.
(4 marks)
List THREE (3) factors that govern the selection of light source and explain
briefly with THREE (3) examples on the implementation of front lighting
sources in Manufacturing. (4 marks)
Given a request to estimate the location of eyes using binary projection
approach. Explain the methodology with illustration to achieve this objective.
(10 marks)
Explain THREE (3) advantages of machine vision systems in industrial
application. (3 marks)
[Total : 25 marks]

This question paper consists of 5 questions on 5 printed pages.
UEMH4333 MACHINE VISION
Q2. (a)
(b)
(c)
(d)
Show with example and explain that redefining starting point of a chain code so
that the resulting sequence of numbers forms an integer of minimum magnitude
makes the code independent of the initial starting point on the boundary.
(10 marks)
Find the normalized shape number of the given difference code:
11076765543322. (2 marks)
An object’s contour may be represented as an ordered list of edges or by a curve.
A curve is a mathematical model for a contour. There are several criteria for a
good contour representation. Briefly explain THREE (3) of them. (6 marks)
Starting at the top left corner, find the shape number of the object shown in
Figure 2.1 below. Determine the order of the shape number. (7 marks)
Total : 25 marks}


Figure 2.1

This question paper consists of 5 questions on 5 printed pages.

UEMH4333 MACHINE VISION
Q3. (a)
(b)
(c)
Hamming Distance is a fast in determining similarity. Define the Hamming
Distance and apply this technique in matching two binary images with
numerical example. (4 marks)
Consider the four vectors x, = (0,0,0)", x. = (1,0,0)", x3 = (4,1,0)7, x, =
(1,0,1)". Calculate the mean vector and covariance matrix by using the
principles of Principal Component Analysis (PCA). Determine the correlation . 1 among the four vectors. [Given Covariance Matrix, C, = = R=1 XRX, -
m,mjy.while K is the number of samples, x, is the input vector and m,, is the
mean vector. | (10 marks)
In order to develop a vision based iris recognition system, apply the knowledge
and techniques from machine vision to stages: acquisition, pre-processing,
feature representation and matching. Explain the potential challenges of this
system and the reason of proposing the respective technique at each stage.
(11 marks)
{Total : 25 marks]
Section-B (Answer ANY ONE (1) question.)
VA Wa. (a)
(b)
(c)
A flat area with center at (X9,¥o) is illuminated by a light source with
intensity distribution:
i(x, y) = Ke7l-%0)*+0-¥o)?]
Image is given by f(x, y) = i(x, y)r(x, y) with reflectance r(x, y) of the area
is constant and equal to 2 and K = 255. Calculate f (x, y). If the resulting image
is digitized with k bits of intensity resolution and our eyes can only detect an
abrupt change of eight shades of intensity between adjacent pixel, calculate
value of k that will cause visible false contouring? (7 marks)
Give the condition(s) under which D, distance between two points p and q is
equal to the shortest 4-path between these points. Determine if the path is
unique. (14 marks)
Application of mean filtering and median filtering produces different effects.
Discuss why a mean filter would be expected to blur an image, while a median
filter would not have this effect. (4 marks)
[Total : 25 marks]

This question paper consists of 5 questions on 5 printed pages.
 UEMH4333 MACHINE VISION
QS. (a)
(b)
(c)
Given a proposed method for circle location involves scanning the image
horizontally, but in this case, for every chord that is found, an estimate is
immediately made of the two points at which the center could lie and votes are
placed at those locations. Construct the geometry equation of this method,
calculate the circle center and briefly explain whether it is faster than the method
that involves scanning the image horizontally and vertically. (10 marks)
Erosion of a set A by structuring element B is a subset of A as long as origin of
B is contained by B. Give an example in which erosion A © B lies outside or
partially outside, A. (6 marks) J
Refer to Figure 5.1, a 3 x 3 region of an image (z’s are the intensity values)
where various masks used to compute the gradient at the point labeled zs.
Assume that Sobel masks are used to obtain g, and gy. Show that the magnitude
of gradient using M(x,y) =.Jgx? + gy? and M(x,y) ~ lal +|ay|] give
identical results. (9 marks)
[Total : 25 marks]

Z4 Z2 23

24 Zs 26

27 Zg Z9
Figure 5.1


This question paper consists of 5 questions on 5 printed pages.
UNIVERSITI TUNKU ABDUL RAHMAN
ACADEMIC YEAR 2022/2023
SEPTEMBER 2022 EXAMINATION
UEMH4333 MACHINE VISION
WEDNESDAY, 28 SEPTEMBER 2022 TIME : 2.00 PM — 4.00 PM (2 HOURS)
BACHELOR OF ENGINEERING (HONOURS) MECHATRONICS ENGINEERING
Instructions to Candidates:
This question paper consists of FIVE (5) questions.
Each question carries 25 marks.
Answer ALL THREE (3) questions from Section-A, and ANY ONE (1) question from Section-B.
 This question paper consists of 5 questions on 5 printed pages.
UEMH4333 MACHINE VISION
Section-A (Answer ALL THREE questions)
Ql. (a) Describe about Machine Vision and FIVE (5) of its main components.
(14 marks)
(b) List THREE (3) factors that govern the selection of light source and explain
with examples FOUR (4) realities that affect Machine Vision System.
(11 marks)
[Total : 25 marks]

Q2. = (a) Given the equation of histogram equalization where every pixel with value r,
is mapped to Sx :
_ Mg-D ok
k~ n x j=o0 Ny;
Where n denote the total number of pixels, ng denote the total number of gray
levels and Ny, the number of pixels in the input image with intensity value 7; .
Apply histogram equalization on the input image of 8 x 8 below. (15 marks)








1/1/5]5|0|0]}1)0
Pitl}2)2/0 ifort
117/616|5|5/0|0
0|7/6)/7/5\)5)5)5
4/7/6)7|3|}5|7|90
1/1)4/1)6)5/6) 1
2f2l4lijilslild
1}2)2]0 0}0) 0) 5
Figure 2.1
(b) Describe with example any five (5) morphological operators used in binary
image processing. (10 marks)
[Total : 25 marks]
 This question paper consists of 5 questions on 5 printed pages.
UEMH4333 MACHINE VISION
Q3. (a)
(b)
(c)
Explain about how the resulting sequence of numbers based on minimum value will help to achieve code independent regardless of starting location at the chain code. (11 marks)
Describe the FOUR (4) main steps in the application of Hough transform in order to locate objects in digital images. (8 marks)
There are several criteria for a good contour representation. Briefly explain THREE (3) of them. (6 marks)
[Total : 25 marks]
This question paper consists of 5 questions on 5 printed pages.
UEMH4333 MACHINE VISION
Section-B (Answer ANY ONE question)
Q4. (a)
(b)
A flat area with center at (Xq, Yo) is illuminated by a light source with intensity
distribution:
i(x,y) = Ke [&-%0)? +(7-¥0)}
Image is given by f(x,y) = i(x, y)r(x, y) with reflectance r(x, y) = 2 of the
area remains constant and equal to 2 and K = 255. Calculate f(x,y). If the
resulting image can be digitized with & bits of intensity resolution and our vision
system only detect an abrupt change of eight shades of intensity between
adjacent pixel, compute the value of & that will cause visible false contouring
that affects the pattern recognition process? (10 marks)
Aspirator as shown in Figure 4.1 moves along a conveyor line for inspection
and packing. The aspirator is ready to be packed and shipped if all the eight
screws are bolted. If you will be given images that is similar to the sample shown
in this figure, propose a solution by applying what you have learned in this
course for detecting screws that are missing. Demonstrate your applied methods
in 3 (THREE) major parts to tackle this problem: pre-processing/enhancement
steps, segment region of interest from background and matching to detect
missing screws. State all assumptions that you make and likely to impact the
solution if necessary. (15 marks)
Figure 4.1
[Total : 25 marks]

This question paper consists of 5 questions on 5 printed pages.
UEMH4333 MACHINE VISION
QS. (a)
(b)
Consider the four vectors x, = (0,0,0)7, x2 = (1,0,0)7, x3 = (1,1,0)", x, =
(1,0,1)". Calculate the mean vector and covariance matrix by using the principles of Principal Component Analysis (PCA) for pattern recognition. Determine the correlation among the four vectors. . . 1 , [Given Covariance Matrix, C, = =z K=1 X_X_ —m,mi while K is the
number of samples, x;, is the input vector and m, is the mean vector]
(11 marks)
Hamming Distance is a fast and effective method to determine similarity.
(i) Define Hamming Distance and its operation between two binary images
with numerical example. (5 marks)
(ii) | Your group mate has used Hamming Distance for measuring the
similarity of two 8-bit grayscale images. He applied Hamming Distance
directly such that the distance between intensity 108 and intensity 110 is 1. Explain whether this method is workable? (5 marks)
(iii) In iris recognition, the iris pattern is extracted from a circular template.
Assuming that the extracted iris features are all in binary form. Head
orientation will cause rotation effect on the binary features. If Hamming
Distance is being applied for matching purpose, apply bit-shifting to
mitigate this effect. Show with numerical example. (4 marks)
[Total : 25 marks]

 This question paper consists of 5 questions on 5 printed pages.
"""

# Remove non-alphanumeric characters and split text into words
words = re.findall(r"\w+", text.lower())

# Initialize a stemmer
stemmer = PorterStemmer()

# Stem the words and count their frequencies
word_count = Counter([stemmer.stem(word) for word in words])

# Sort words by their count in descending order
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# Print the sorted words and their counts
for word, count in sorted_words:
    if len(word) > 4:
        print(f"{word}: {count}")
