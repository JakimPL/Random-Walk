from randomwalk import RandomWalk

print("Generating a random walk...")
random_walk = RandomWalk()
length = random_walk.length
steps = random_walk.config.steps
output_directory = random_walk.config.output_directory
data_filename = output_directory + "/walk.txt"

print("A random walk generated successfully. Exporting data to {0} filename...".format(data_filename))
random_walk.export_walk(data_filename)

print("Exporting the plot to {0} directory...".format(output_directory))
random_walk.make_plot(output_directory, steps)

print("Generating a sound wave to {0} directory...".format(output_directory))
random_walk.make_sound(output_directory, steps)

print("Random walk generator ends.")
