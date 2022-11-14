# ITV_Hub Assessment

This assessment accepts input json data that stores videoplay events and returns the maximum number of videos playing at the same time.

### Assumptions for generating the json data
- videoplay events happened within a month (April was used)
- videos can be of unequal lengths
- start times are used to determine the videos playing together at the same time since video lengths are assumed to be unequal.

### Dataset
The dataset used is generated randomly using a python code located in the data_generator folder.

![image](https://user-images.githubusercontent.com/30020704/201565640-fc747ce4-dde7-4de8-a852-144a5ae99c11.png)

### How to run
This project uses `venv` in other for users to easily run.
To run locally:
```sh
    git clone project repository
    create virtual environment using `python3 -m venv env` for macos/unix and `py -m venv env` for windows 
    activate the virtual environment using `env/Scripts/activate.bat` or `source/env/bin/activate`
    RUN `pip install -e .`
```

### Steps to run the code
```sh
cd into root folder
RUN `max-video-cli`
```


### Alternative way to run the code
I created an API endpoint to wrap the function.

```sh
cd into root folder
RUN `uvicorn source.project_script.max_video_play:app`
Go to `http://localhost:8000/videoplay` on your browser
```


### Steps to run the integration test
```sh
cd into root folder
RUN `pip install -r requirements_dev.txt`
RUN `pytest`
```

##### Expected result(maximum number of videos playing at once)
![image](https://user-images.githubusercontent.com/30020704/202834089-28c9d336-e6fb-4f85-a472-5b5951fe1318.png)


##### Expected result from the API(maximum number of videos playing at once)
![image](https://user-images.githubusercontent.com/30020704/202834128-80af8895-173e-4210-b627-c556e0e75c77.png)


##### Expected test output
![image](https://user-images.githubusercontent.com/30020704/202834039-82d94cf2-89d9-42b6-ae43-11f5ee908dc9.png)


##### This project uses github action for continuous integration
![image](https://user-images.githubusercontent.com/30020704/201562005-e2a11972-41bc-4548-834a-652884519c44.png)


### Tools and Technologies used:
- Language - Python

Writing by:
- Mujeeb Adeniji