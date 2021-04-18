import json


class Config:
    def __init__(self):
        with open("config.json", 'r') as filename:
            config_data = json.load(filename)
            self.length = config_data['walk_length']
            self.steps = config_data['steps']
            self.sampling_frequency = config_data['sampling_frequency']
            self.frame_rate = config_data['frame_rate']
            self.frequency_min = config_data['frequency_min']
            self.frequency_max = config_data['frequency_max']
            self.output_directory = config_data['output_directory']
