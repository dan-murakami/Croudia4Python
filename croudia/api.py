import requests

class API:
    """docstring for API"""
    def __init__(self, consumer_key, consumer_secret, access_token='', access_token_secret='',
            endpoint='https://api.croudia.com'):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.endpoint = endpoint
        if access_token != '' and access_token_secret != '':
            self.set_access_token(access_token, access_token_secret)

    def set_access_token(self, access_token, access_token_secret):
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def get_access_token(self):
        return self.access_token, self.access_token_secret

    def request_access_token(self, grant_type='authorization_code',
            client_id=self.consumer_key, client_secret=self.consumer_secret, code='', refresh_token=''):
        if grant_type == 'authorization_code':
            return self.do('post', '/oauth/token',
            {'grant_type': grant_type, 'client_id': client_id, 'client_secret': client_secret, 'code': code})
        else:
            return self.do('post', '/oauth/token',
            {'grant_type': grant_type, 'client_id': client_id, 'client_secret': client_secret, 'refresh_token': refresh_token})

    def do(self, method, url, args={}):
        pass
