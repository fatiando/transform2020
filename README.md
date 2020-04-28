# From scattered data to gridded products using Verde

Material for the [Verde tutorial at Transform 2020](https://sched.co/c7KE).

## About

This tutorial will be a hands-on tour of [Verde](https://www.fatiando.org/verde/), 
a Python package for processing and gridding geophysical/geospatial data with a 
twist of machine learning. We'll use a mix of live coding, short exercises, and 
pair activities (note that this may change as the tutorial is developed). 

We'll start with a real dataset and work our way towards producing one or more 
gridded products. The way there will take us through:

* Generating and handling coordinates
* Data decimation with blocked means/medians to avoid aliasing
* 2D trend estimation
* Splitting training and testing data for validation
* Gridding with bi-harmonic splines
* Cross-validation of data distrubuted spatially on the Earth
* Combining everything into a pipeline

## What you'll need

* Some knowledge of Python will help (for example, you might want to attend 
  [this](https://transform2020.sched.com/event/c7Jm/getting-started-with-python) or 
  [this](https://transform2020.sched.com/event/c7Jn/more-python-for-subsurface) tutorial).
* We'll use [xarray](http://xarray.pydata.org/), [matplotlib](https://matplotlib.org/), 
  and [cartopy](https://scitools.org.uk/cartopy/docs/latest/) in this tutorial. 
  You don't need to be an expert in these tools but some familiarity will help.
* All coding will be done in Jupyter notebooks. I'll explain how they work briefly but 
  it will help if you've used them before.

Instructions for setting up your computer will follow. 
There will also be instructions for [Google Colab](https://colab.research.google.com/) or 
[Binder](https://mybinder.org/) in case you want/have to run the code online.

## Where to get the material

The Jupyter notebooks and any other required material will be included in this GitHub 
repository: [github.com/fatiando/transform2020](https://github.com/fatiando/transform2020/)

## How this will work

More details to follow. For now, I'm anticipating to have:

* Live coding through a Zoom call.
* Shared note taking on Google Docs or HackMD (where I'll post links and assignments).
* Chat on the Software Underground slack.
* Short pair programming exercises (if the Zoom call allows breakout rooms).

## License

All code and text in this repository is free software: you can redistribute it and/or 
modify it under the terms of the BSD 3-clause License. 
A copy of this license is provided in [LICENSE](https://github.com/fatiando/transform2020/blob/master/LICENSE).
