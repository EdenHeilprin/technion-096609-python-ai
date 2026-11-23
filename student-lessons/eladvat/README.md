# Matplotlib - figures

**Presenter(s):** Elad Vaturi

**Length:** 40–50 minutes, including the live example, activity, questions, and discussion.

on many occations, we need to extract data into a specific figure. This tool enables custom figure creation in different ways (bar, scatter, histogram etc.)
One clear advantage this has over SPSS, for example, is once you create the custom figure - you can use the same code to redo it again and again, even after the data itself changes.

## By the end of this lesson

- you will be able to import a dataset and use matplotlib to turn it into your own custom figure.
- change properties of a figure
- reuse your script after a data change and see the figure update.

## Get ready


1. download the lesson folder and open it in VS code as your working folder.
2. install MAPLOTLIB in your project - paste the following into a new terminal:
```
pip install matlplotlib
```
- (this tells the Python Install Package, or PIP, to find matplotlib and install it for you)  
  
3. create a new python file. try to import matplotlib by adding this code:
```
import matplotlib.pyplot as plt
```
then run the file. if installed correctly, you should see no errors.  
if the error *ModuleNotFoundError: No module named 'matplotlib'* is displayed, this means maplotlib is missing.

note: in this lesson we only import pyplot from matplotlib, since all the basic tools we need are already there. advanced cases might require other parts of matplotlib.
## A worked example
today we will use real data that was gathered in israel in late 2023. this data describes scores of anxiety, depression and psychological needs among evacuated and non-evacuated people, along with some demographics.  
split up into three groups. each group will open a different demo file: bar plot, box plot or scatter plot.
run the demo and examine the result. then think together about an improvement you'd like to make to the figure, or a different research question (on the current data) you'd want to look into with your figure type.
**Expected result:** each demo produces a basic figure in a new window. notice the axis labels and the different attributes of the figure - almost anything can be changed here.

## Try it yourself
each group will now change/add one variable in their figure *manually*. look for their mentions in the code and edit accordingly.  
also, change the color of your figure to something nicer. 
make sure to update labels and titles!

### Advanced tasks - use AI for those:
barplot:
- change it to an interaction graph (2x2). example: region + evacuation -> anxiety.
- add error bars of 95% CI.  

histogram: 
- create a split histogram - show frequencies of one of the DVs, color-coded by one of the categorial IVs.  

scatterplot: 
- add a regression line.

<details>
<summary>Answer and discussion</summary>
now you should have a new figure which describes your chosen analysis, is clear, has matching labels and titles, and looks great.
each group/person will tell what they did in their figure (share your screen!) and what they learned can be changed about it.
</details>

## Quick reference

| Tool or idea | What it does |
| --- | --- |
| plt.figure() | prepares new figure space |
| plt.bar(x, y) | bar plot |
| plt.hist(x) | histogram |
| plt.boxplot([Y1, Y2]) | box plot |
| plt.scatter(x, y) | scatter plot |
| plt.xlabel(""), plt.ylabel("") | edit axis labels |
| plt.title("") | edit figure title |
| plt.show() | show figure |

## Sources and further learning

- [official matplotlib website](https://matplotlib.org/)
- [matplotlib tutorials on w3schools](https://www.w3schools.com/python/matplotlib_intro.asp)
- [matplotlib tutorials on campusIL (requires sign-in)](https://app.campus.gov.il/learning/course/course-v1:CS+GOV_CS_Data_DataIntro101_HE+2022_2/home)
