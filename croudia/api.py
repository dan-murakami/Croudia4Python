import requests
from requests_oauthlib import OAuth2Session

class API:
    """docstring for API"""
    def __init__(self, consumer_key, consumer_secret, access_token='', refresh_token='',
            endpoint='https://api.croudia.com/', oauth=None):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.endpoint = endpoint
        self.oauth = oauth

    def get_authorization_url(self, state=''):
        return self.endpoint+'oauth/authorize?response_type=code&client_id='+self.consumer_key+('&state='+state if state else '')

    def request_access_token(self, grant_type='authorization_code', code='', refresh_token=''):
        if grant_type == 'authorization_code':
            r = requests.post(self.endpoint+'oauth/token',
            params={'grant_type': grant_type, 'client_id': self.consumer_key, 'client_secret': self.consumer_secret, 'code': code})
        else:
            r = requests.post(self.endpoint+'oauth/token',
            params={'grant_type': grant_type, 'client_id': self.consumer_key, 'client_secret': self.consumer_secret, 'refresh_token': refresh_token})
        rj = r.json()
        if rj:
            if 'error' in rj:
                raise Error
            else:
                self.oauth = OAuth2Session(self.consumer_key, token=rj)

    def get(self, url, params={}):
        return self.oauth.get(self.endpoint+url, params=params).json()

    def post(self, url, params={}, files={}):
        return self.oauth.post(self.endpoint+url, params=params, files=files).json()
