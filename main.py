import os
import re
import subprocess
from datetime import datetime
from randomwalk import RandomWalk


print("Generating a random walk...")
random_walk = RandomWalk()
length = random_walk.length
steps = random_walk.config.steps

date_time = re.sub('[^0-9]', '_', str(datetime.now()))
output_directory = "{0}/{1}".format(random_walk.config.output_directory, date_time)
os.mkdir(output_directory)
data_filename = output_directory + "/walk.txt"
avi_filename = output_directory + "/walk.avi"

print("A random walk generated successfully. Exporting data to '{0}' file...".format(data_filename))
random_walk.export_walk(data_filename)

print("Exporting the plot to '{0}/' directory...".format(output_directory))
random_walk.make_plot(output_directory, steps)

print("Generating a sound wave to '{0}/' directory...".format(output_directory))
random_walk.make_sound(output_directory, steps)

print("Converting images to '{0}' avi file...".format(avi_filename))
subprocess.Popen(["./png2avi.sh {0} {1}".format(date_time, random_walk.config.frame_rate)], shell=True)

print("Random walk generator ends.")
