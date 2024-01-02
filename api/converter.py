import pandas as pd
import json

# json_data = '{"Data":[{"id":3,"date":"1402-09-16","start_time":"10:30:00","end_time":"17:30:00"}],"Message":null}'

def convert_json_to_data(json_data):
    df = pd.read_json(json_data)

    date_value = df['Data'][0]['date']
    start_time_value = df['Data'][0]['start_time']
    end_time_value = df['Data'][0]['end_time']

    # print("Date:", date_value)
    # print("Start Time:", start_time_value)
    # print("End Time:", end_time_value)
