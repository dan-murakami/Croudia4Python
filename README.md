# Croudia4Python
A Croudia's API Wrapper for Python 3.x

## Requirements
- [requests](http://requests-docs-ja.readthedocs.org/en/latest/)
- [requests_oauthlib](https://github.com/requests/requests-oauthlib)

## How to use
### Initialization
```python
# import this.
import croudia

CONSUMER_KEY = 'set your consumer key'
CONSUMER_SECRET = 'set your consumer secret'

# create your API wrapper
api = croudia.API(CONSUMER_KEY, CONSUMER_SECRET)

# get authorization url to get access token
url = api.get_authorization_url()
print("Please access to ", url)

# then, get your access token with the code you have got
api.request_access_token(code=input('code : '))
```