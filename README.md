# This is the TeamZ AI Jam Repo
Yang Wen, Luke Dicken

## A City History Generator for Minecraft

Our project integrates [Tracery](http://tracery.io/) with the [Generative Design in Minecraft](http://gendesignmc.engineering.nyu.edu/) system.

We leverage Tracery to create a narrative about the city. We use a rich grammar which is available in [tracery_minecraft.py](https://github.com/gameaischool2019members/TeamZ/blob/master/tracery_settlement.py) and build interesting details about the city, both from a narrative and data point of view. Not only does the city have generate elements around things like its name and initial size, but it also has randomized encounters which affect the underlying data such as the population.

This data model is made available to the [MCEdit](https://www.mcedit.net/) filter [TeamZ.py](https://github.com/gameaischool2019members/TeamZ/blob/master/stock-filters/TeamZ.py) developed based on some of the provided examples. This allows us to have a generative system, informed by the narrative arc of the city and its history.

Obviously with only 1.5 days available, this is far from robust, but the team is happy to have picked up two tools that we had not previously had excuse to use and to make something work, despite being pretty janky :) 

## Images

![story1](https://github.com/gameaischool2019members/TeamZ/raw/master/screenshots/story1.png)
![city1](https://github.com/gameaischool2019members/TeamZ/raw/master/screenshots/city1.png)
![sign1](https://github.com/gameaischool2019members/TeamZ/raw/master/screenshots/sign1.png)
![city2](https://github.com/gameaischool2019members/TeamZ/raw/master/screenshots/city2.png)
![story2](https://github.com/gameaischool2019members/TeamZ/raw/master/screenshots/story2.png)
