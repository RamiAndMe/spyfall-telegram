# Allow Python to Send HTTP request
import requests

# Pretty Printer
from pprint import pprint

# Setting up some variables...
BOT_TOKEN = '<1939656470:AAGPRsDVZMqvKBlhul_Bd_1Xxgen-K8DHzg'
BOT_URL = 'https://api.telegram.org/cesusbot' + BOT_TOKEN + '/'


# Send Message (/sendMessage)
data = {
    'chat_id': <Insert Chat ID>,
    'text': <Write whatever you want>
}
response = __________________

# Print Response
pprint(response.json())
