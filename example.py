import croudia
import webbrowser

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

api = croudia.API(CONSUMER_KEY, CONSUMER_SECRET)
webbrowser.open(api.get_authorization_url())
api.request_access_token(code=input('code : '))

api.post('2/statuses/update.json', {'status': 'Hello, Croudia for Python!'})