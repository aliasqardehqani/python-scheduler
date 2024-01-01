import requests
from exceptions import APIException



def call_api_with_body(url, api_token, channel_id):
    try:
        headers = {'Authorization': f'Bearer {api_token}'}
        payload = {'channel_id': channel_id}

        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            return response.text
        else:
            raise APIException(f"Error: Unable to call API. Status Code: {response.status_code}")

    except requests.exceptions.RequestException as req_exception:
        print(f"Request Exception: {req_exception}")

    except APIException as custom_exception:
        print(custom_exception)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = 'api_url'
    api_token = 'token'  
    channel_id = ''
    
    call_api_with_body(url, api_token, channel_id)
