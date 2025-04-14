'''
plot.py
This file contains the plot class that is used to plot the data.
This file is used to compare the lap times of two different types of followers:
Takes in data from the main file, line follower and wall follower.
This file is used to plot the data using matplotlib.
'''

class plotData:
    def __init__(self, datain1, datain2):
        self.datain1 = datain1
        self.datain2 = datain2

    def plot(self):
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 6))
        bins = 5  
        plt.hist(self.datain1, bins=bins, alpha=0.6, label='Line Follower', color='blue', edgecolor='black')
        plt.hist(self.datain2, bins=bins, alpha=0.6, label='Wall Follower', color='orange', edgecolor='black')

        plt.title("Lap Time Comparison: Line vs Wall Follower")
        plt.xlabel("Lap Time (seconds)")
        plt.ylabel("Frequency")
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.savefig("lap_time_histogram.png")