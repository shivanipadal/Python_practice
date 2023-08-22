import requests

from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        res=requests.get(url)
        res.raise_for_status()
    except HTTPError as http_err :
        print(f'Http error occured: {http_err}')
    except Exception as err :
        print(f'Other error occured: {err}')
    else:
        print(f'Success! for {url}')



