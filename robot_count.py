#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import os.path
from time import strftime, localtime
from bs4 import BeautifulSoup


filename = strftime("%Y-%m-%d %H:%M:%S", localtime())
folder = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "Robot Counts/")

record = open(folder + filename, "w")
record.write(filename + "\n\nRobot Counts:\n\n")

url = "http://www.ituro.org/tr/"
html = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(html, "lxml")

category_list = soup.findAll("th", attrs={'class': "col-md-1 text-center"})
categories = [category.text for category in category_list]

robot_list = soup.findAll("td")
robots = [int(robot.text) for robot in robot_list]

robot_counts = dict(zip(categories, robots))

for robot in robot_counts:
    record.write(robot + ": " + str(robot_counts[robot]) + "\n")

record.write("\n\nTotal: " + str(sum(robots)))
record.close()
