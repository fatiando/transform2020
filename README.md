# From scattered data to gridded products using Verde

The [Verde tutorial at Transform 2020](https://sched.co/c7KE) 💚

**Instructors:**
[Leonardo Uieda](https://www.leouieda.com/)<sup>1</sup> and
[Santiago Soler](https://santisoler.github.io/)<sup>2</sup>

> <sup>1</sup>Department of Earth, Ocean and Ecological Sciences, School of Environmental Sciences, University of Liverpool, UK<br>
> <sup>2</sup>CONICET, Argentina | Instituto Geofísico Sismológico Volponi, Universidad Nacional de San Juan, Argentina

|         | Info |
|--------:|:-----|
| When    | Thursday, June 11 • 08:00 - 11:00 GMT |
| Slack   | [Software Underground](https://softwareunderground.org/) channel `t20-thu-verde` |
| YouTube | https://youtu.be/-xZdNdvzm3E |
| conda environment  | `t20-thu-verde` |


## BEFORE THE TUTORIAL

Make sure you've done these things **before the tutorial on Thursday**:

1. Sign-up for the [Software Underground Slack](https://softwareunderground.org/slack)
1. Join the channel `t20-thu-verde`. This is where **all communication will
   happend**.
1. Set up your computer ([intructions below](#setup)). We will not have time to
   solve many computer issues during the tutorial so make sure you do this
   ahead of time. If you need any help, ask at the `t20-thu-verde` channel on
   Slack.
1. If you have some data you'd like to process, please have it ready and make
   sure you can load it with pandas or numpy. You'll have some time at the end
   of the tutorial to work on your own data.

## About

This tutorial will be a hands-on tour of
[Verde](https://www.fatiando.org/verde/), a Python package for processing and
gridding geophysical/geospatial data with a twist of machine learning. We'll
start with a real dataset and work our way towards producing one or more
gridded products. The way there will take us through:

* Loading some data
* Generating and handling coordinates and projections (using pyproj)
* Splitting training and testing data for validation
* Data decimation with blocked means/medians to avoid aliasing
* 2D trend estimation
* Gridding with bi-harmonic splines
* Combining everything into a data processing pipeline
* Cross-validation of data distributed spatially on the Earth (including
  parallel execution with Dask)

## Prerequisites

* Some knowledge of Python is assumed (for example, you might want to attend
  [this](https://transform2020.sched.com/event/c7Jm/getting-started-with-python) or
  [this](https://transform2020.sched.com/event/c7Jn/more-python-for-subsurface) tutorial).
* All coding will be done in Jupyter notebooks. I'll explain how they work
  briefly but it will help if you've used them before.
* We'll use [numpy](https://numpy.org/), [pandas](https://pandas.pydata.org/),
  [xarray](http://xarray.pydata.org/), and [matplotlib](https://matplotlib.org/).
  You don't need to be an expert in these tools but some familiarity will help.

## Setup

Follow the Transform guidelines. Create a conda env.
Instructions for setting up your computer will follow.
There will also be instructions for [Google Colab](https://colab.research.google.com/) or
[Binder](https://mybinder.org/) in case you want/have to run the code online.

## How the tutorial will work

Due to the number of participants, we can't do anything too interactive.
Instead, we'll do a brief introduction, some live coding using an example
dataset with a couple of exercises in the middle, and finally you'll have
time to work on your own data (or another example dataset).

| Time          | Activity |
|:-------------:|:---------|
|  8:00 -  8:20 | Introduction |
|  8:20 -  9:00 | Loading data, projections, slicing, blocked reductions, trends |
|  9:00 -  9:20 | Break |
|  9:20 - 10:00 | Train-test-split, gridding, cross-validation, hyper-parameter optimizationa |
| 10:00 - 10:10 | Wrap-up: state of the project, future directions, how to get involved |
| 10:10 - 11:00 | Q&A on Slack, work on your own data, informal chat |

## License

All code and text in this repository is free software: you can redistribute it and/or
modify it under the terms of the BSD 3-clause License.
A copy of this license is provided in [LICENSE](https://github.com/fatiando/transform2020/blob/master/LICENSE).
