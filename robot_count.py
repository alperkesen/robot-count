#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import localtime
from bs4 import BeautifulSoup
import urllib.request


filename = str(localtime()[2]) + "-" + str(localtime()[1]) + \
           "-" + str(localtime()[0]) + "_" + str(localtime()[3]) + \
            ":" + str(localtime()[4]) + ".txt"

folder = "/home/alper/Documents/Robot Count System/Robot Counts/"

file = open(folder + filename, "w")

file.write(str(localtime()[2]) + "/" + str(localtime()[1]) + \
           "/" + str(localtime()[0]) + "  Time: " + str(localtime()[3]) \
           + ":" + str(localtime()[4]) + "\n\nRobot Count List:\n\n")

url = "http://www.ituro.org/tr/"
html = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(html)

category_list = soup.findAll("th", attrs={'class': "col-md-1 text-center"})
categories = []

robot_list = soup.findAll("td")
robots = []

for category in category_list:
    categories.append(category.text)

for robot in robot_list:
    robots.append(int(robot.text))
    
robot_counts = dict(zip(categories, robots))

for robot_count in robot_counts:
    file.write(robot_count + ": " +str(robot_counts[robot_count]) + "\n")
file.write("\n\nToplam : " + str(sum(robots)))

file.close()
