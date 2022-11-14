import json
from collections import Counter



def max_num_videos_playing_together():
    """This function returns the maximum number of videos playing at once and the date and time"""
    filepath = './source/data_generator/data_source_file/videoplay.json'
    with open(filepath) as f:
        data = json.load(f)
        counter = Counter(item.get('startTime') for item in data['videoPlay'])
        data_list = counter.most_common()
        max_num_of_videos = max(data_list, key=lambda tup: tup[1])
        return f"The maximum number of videos playing at once is: {max_num_of_videos[1]}, and at date and time: {max_num_of_videos[0]}"


if __name__ == '__main__':
    max_num_videos_playing_together()
