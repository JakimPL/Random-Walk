import colorsys
import math
import random
import matplotlib.pyplot as plot


class RandomWalk:
    def __init__(self, n):
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        x = 0
        y = 0
        self.walk = [[0, 0] for _ in range(n)]
        for i in range(n):
            self.walk[i] = [x, y]
            direction = directions[random.randint(0, 3)]
            x += direction[0]
            y += direction[1]

        self.data = self.transpose()

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
                random_walk.walk += [list(map(int, item))]
                line = file.readline()
        random_walk.data = random_walk.transpose()
        return random_walk

    def make_plot(self, directory="", steps=0):
        plot_range = self.get_range(2)
        n = len(self.walk)

        figure = plot.figure(figsize=(plot_range[0][1] - plot_range[0][0], plot_range[1][1] - plot_range[1][0]))
        figure.patch.set_facecolor('black')
        plot.xlim(plot_range[0])
        plot.ylim(plot_range[1])
        plot.axis('off')
        step = 0

        path = directory + '/'
        r = len(str(steps))
        for i in range(n - 1):
            color = colorsys.hsv_to_rgb(i / n, 1.0, 1.0)
            if steps > 0 and i / n >= step / steps:
                step += 1
                plot.savefig(path + str(step).rjust(r, '0'))

            plot.plot(self.data[0][i:i + 2], self.data[1][i:i + 2], color=color, linewidth=12)

        if directory:
            plot.savefig(path + (str(step).rjust(r, '0') if steps > 0 else 'walk'))
        else:
            plot.show()
