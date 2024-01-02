import requests
import json
# import sys
# print(sys.path)

from exceptions import APIException
from converter import convert_json_to_data


def call_api_with_body(url, api_token, channel_id):
    try:
        headers = {'Authorization': f'Bearer {api_token}'}
        payload = {'channel_id': channel_id}

        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            print(response.text)
            return convert_json_to_data(response.text)
        else:
            raise APIException(f"Error: Unable to call API. Status Code: {response.status_code}")

    except requests.exceptions.RequestException as req_exception:
        print(f"Request Exception: {req_exception}")

    except APIException as custom_exception:
        print(custom_exception)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    
    url = 'api_urls'
    api_token = 'token'  
    channel_id = 'channelID'
    
    call_api_with_body(url, api_token, channel_id)



# {"Data":[{"id":3,"date":"1402-09-16","start_time":"10:30:00","end_time":"17:30:00"}],"Message":null}