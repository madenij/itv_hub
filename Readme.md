# ITV_Hub Assessment

This assessment accepts input json data that stores videoplay events and returns the maximum number of videos playing at the same time.

### Assumptions for generating the json data
- videoplay events happened within a month (April was used)
- videos can be of unequal lengths
- start times are used to determine the videos playing together at the same time since video lengths are assumed to be unequal.

### Dataset
The dataset used is generated randomly using a python code located in the data_generator folder.

### How to run
This project uses `venv` in other for users to easily run.
To run locally:
```sh
    git clone project repository
    create virtual environment using `virtualenv venv`
    activate the virtual environment using `venv /Scripts/activate.bat`
    RUN `pip install -e .`
```

### Steps to run the code
```sh
cd into root folder
RUN max-video-cli
```
- Running the above will generate an output in form of 'The maximum number of videos playing at once is: `num`, and at date and time: `datetime`'

### Steps to run the integration test
```sh
cd into root folder
RUN pytest
```

### This project uses github action for continuous integration
image.png

### Tools and Technologies used:
- Language - Python

