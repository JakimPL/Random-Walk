import colorsys
import math
import random
import matplotlib.pyplot as plot
from config import Config
from progress import progress_bar
from sound import Sound


class RandomWalk:
    def __init__(self, n=0):
        self.config = Config()
        self.mode = self.config.mode

        if n == 0:
            n = self.config.length

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        x = 0
        y = 0
        self.walk = [[0, 0] for _ in range(n)]
        for i in range(n):
            self.walk[i] = [x, y]

            if self.mode:
                direction = [2 * random.random() - 1, 2 * random.random() - 1]
            else:
                direction = directions[random.randint(0, 3)]

            x += direction[0]
            y += direction[1]

        self.data = self.transpose()
        self.length = len(self.walk)

    def transpose(self):
        return list(map(list, zip(*self.walk)))

    def get_range(self, offset=0):
        return [[min(self.data[0]) - offset, max(self.data[0]) + offset],
                [min(self.data[1]) - offset, max(self.data[1]) + offset]]

    def export_walk(self, filename):
        with open(filename, 'w') as file:
            for item in self.walk:
                file.write("{0}, {1}\n".format(item[0], item[1]))

    @staticmethod
    def import_walk(filename):
        random_walk = RandomWalk(0)
        with open(filename, 'r') as file:
            line = file.readline()
            while line:
                item = line.strip().split(',')
                random_walk.walk += [list(map(float, item))]
                line = file.readline()
        random_walk.data = random_walk.transpose()
        random_walk.length = len(random_walk.walk)
        return random_walk

    def make_plot(self, directory="", steps=0):
        path = directory + '/'
        n = self.length
        r = len(str(steps))

        plot_range = self.get_range(self.config.plot_offset)
        figure = plot.figure(figsize=(plot_range[0][1] - plot_range[0][0], plot_range[1][1] - plot_range[1][0]))
        figure.patch.set_facecolor(self.config.plot_background_color)
        plot.xlim(plot_range[0])
        plot.ylim(plot_range[1])
        plot.axis('off')
        step = 0

        for i in range(n - 1):
            color = colorsys.hsv_to_rgb(i / n, 1.0, 1.0)
            if steps > 0 and i / n >= step / steps:
                step += 1
                plot.savefig(path + str(step).rjust(r, '0'))
                progress_bar(step, steps)

            plot.plot(self.data[0][i:i + 2], self.data[1][i:i + 2], color=color, linewidth=self.config.plot_line_width)

        if directory:
            plot.savefig(path + (str(step).rjust(r, '0') if steps > 0 else "walk"))
        else:
            plot.show()

        if steps > 0:
            print('\n')

    def make_sound(self, directory, steps=0):
        if steps == 0:
            return

        path = directory + '/'
        n = self.length

        walk_range = self.get_range()

        def x(value):
            return (value - walk_range[0][0]) / (walk_range[0][1] - walk_range[0][0])

        def y(value):
            return (value - walk_range[1][0]) / (walk_range[1][1] - walk_range[1][0])

        def frequency(value, frequency_min=self.config.frequency_min, frequency_max=self.config.frequency_max):
            return frequency_min * ((frequency_max / frequency_min) ** y(value))

        duration = 1 / self.config.frame_rate
        sound = Sound(sampling_frequency=self.config.sampling_frequency, note_duration=duration)
        for i in range(steps + 1):
            index = math.ceil(i * (n / steps)) if i < steps else -1
            point = self.walk[index]
            note = [frequency(point[1]), x(point[0])]
            sound.make_sound(note[0], note[1])
            progress_bar(i, steps)

        sound.export_sound(path + "walk.wav")
        print('\n')
