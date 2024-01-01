"""
    This code for call api from master project.
"""

import requests
from exceptions import APIException


def call_api(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            print("API Response:")
            print(response.text)
        else:
            raise APIException(f"Error: Unable to call API. Status Code: {response.status_code}")
        
    except requests.exceptions.RequestException as req_exception:
        print(f"Request Exception: {req_exception}")
        
    except APIException as custom_exception:
        print(custom_exception)
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    
    api_url = 'http://178.131.94.27:13123/api/device/check-value-sensor/'
    call_api(api_url)
