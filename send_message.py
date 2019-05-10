# Allow Python to Send HTTP request
import requests

# Pretty Printer
from pprint import pprint

# Setting up some variables...
BOT_TOKEN = '<Insert your bot token here>'
BOT_URL = 'https://api.telegram.org/bot' + BOT_TOKEN + '/'


# Send Message (/sendMessage)
data = {
    'chat_id': <Insert Chat ID>,
    'text': <Write whatever you want>
}
response = __________________

# Print Response
pprint(response.json())