import croudia
import webbrowser

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

api = croudia.API(CONSUMER_KEY, CONSUMER_SECRET)
webbrowser.open(api.get_authorization_url())
api.request_access_token(code=input('code : '))

# Whisper
api.post('2/statuses/update.json', {'status': 'Hello, Croudia for Python!'})

# Get whispers in your timeline
for s in api.get('2/statuses/home_timeline.json'):
    print(s)