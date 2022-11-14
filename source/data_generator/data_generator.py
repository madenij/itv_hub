import json
import datetime
from datetime import timedelta
import random

n = 30
data={
    "videoPlay": []
}

for _ in range(n):
    """Generate random start times and end times for each videoplay events"""
    start_date = start_date = datetime.datetime(2022, 4, 1)
    end_date = datetime.datetime(2022, 4, 30)
    start = start_date + (end_date - start_date) * random.random()
    end = start + timedelta(hours = 3)
    new_start = start.strftime("%Y-%m-%dT%H:%M:%S")
    new_end = end.strftime("%Y-%m-%dT%H:%M:%S")
    data["videoPlay"].append(
        {
            "startTime": new_start,
            "endTime": new_end
    })

with open('data_source_file/videoplay.json', 'w') as outfile:
    """Write the generated data to a json file"""
    json.dump(data, outfile)
