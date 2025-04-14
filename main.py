'''
Main file for the project
This file contains the main function that runs the program.
It imports the plot class and calls the plot function to plot the data.
This file is used to compare the lap times of two different types of followers:
Line follower and Wall follower. Man copilot for comments is nice
'''

#improts
import matplotlib.pyplot as plt
import plot

#input data for line follower
line_follower_times = [
    11.34, 11.43, 11.47, 11.42, 11.39, 11.44, 11.43, 11.45, 11.48, 11.40,
    11.44, 11.52, 11.46, 11.44, 11.38, 11.42, 11.49, 11.42, 11.50, 11.41,
    11.46, 11.58, 11.50, 11.48, 11.44, 11.42, 11.52, 11.48, 11.51, 11.51
]

#input data for wall follower
wall_follower_times = [
    11.00, 11.17, 11.08, 11.10, 11.09, 11.22, 11.02, 11.02, 11.07, 11.10,
    11.06, 11.18, 11.10, 11.08, 11.14, 11.24, 11.05, 11.07, 11.10, 11.11,
    11.07, 11.18, 11.14, 11.18, 11.14, 11.00, 11.07, 11.13, 11.14, 11.12
]

#call plot class to plot
plotter = plot.plotData(line_follower_times, wall_follower_times)
plotter.plot()