import math
import struct
import wave


class Sound:
    sampling_frequency = 44100
    note_duration = 0.1
    sample = []

    def make_sound(self, frequency, harmonics):
        size = self.sampling_frequency * self.note_duration
        for x in range(int(size)):
            y_sin = math.sin(2 * math.pi * frequency * (x / self.sampling_frequency))
            y_saw = 2 * (x % (self.sampling_frequency / frequency)) * frequency / self.sampling_frequency - 1
            y = (y_sin * (1 - harmonics) + y_saw * harmonics) / 2
            self.sample.append(y)

    def export_sound(self, filename):
        with wave.open(filename, 'w') as file:
            file.setparams((1, 2, self.sampling_frequency, len(self.sample), "NONE", "not compressed"))
            for x in self.sample:
                file.writeframes(struct.pack('h', int(65536 * x / 2)))
