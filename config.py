import json


class Config:
    def __init__(self):
        with open("config.json", 'r') as filename:
            config_data = json.load(filename)
            self.output_directory = config_data['output_directory']
            self.length = config_data['random_walk']['walk_length']
            self.steps = config_data['random_walk']['steps']
            self.mode = config_data['random_walk']['mode']
            self.sampling_frequency = config_data['sound']['sampling_frequency']
            self.frame_rate = config_data['sound']['frame_rate']
            self.frequency_min = config_data['sound']['frequency_min']
            self.frequency_max = config_data['sound']['frequency_max']
            self.plot_offset = config_data['plot']['offset']
            self.plot_line_width = config_data['plot']['line_width']
            self.plot_background_color = config_data['plot']['background_color']
