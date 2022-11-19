import pytest
import json
from source.project_script.max_video_play import *



def test_generated_input_data():
    '''Test that the generated input data is a json file, and contains fields: startTime and endTime'''
    filepath = './source/data_generator/data_source_file/videoplay.json'
    with open(filepath) as f:
        data = json.load(f)
        assert isinstance(data, dict)
        assert 'startTime' in data['videoPlay'][0]
        assert 'endTime' in data['videoPlay'][0]


def test_returned_maxmum_number_of_video_played_together():
    '''Test that the function returns a string'''
    assert isinstance(max_num_videos_playing_together(), dict)
    

