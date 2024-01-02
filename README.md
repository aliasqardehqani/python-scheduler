# Python scheduler
We needed a scheduler section in our main project. We decided to separate it with microservices. This was the best opportunity to display it as a repository.
## Installation
```
    pip install schedule
    pip install pandas
```

## CallAPi 

    1. Call an api from the django web server and get the json.
    2. Extract 3 values ​​from json with pandas. Values ​​= [1-date, 2-start time, 3-end time]
    2. Send values ​​for scheduling in start and end time.
