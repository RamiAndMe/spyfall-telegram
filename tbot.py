from pprint import pprint

import requests

class TBot:    
    def __init__(self, TOKEN):
        self.TOKEN = TOKEN
        self.URL = 'https://api.telegram.org/bot' + TOKEN + '/'

        self.keyboardMarkup = None

        self.last_update_id = None

    def set_keyboard_markup(self, keyboard, resize_keyboard=None, one_time_keyboard=None, selective=None):
        if not(isinstance(keyboard, list) and isinstance(keyboard[0], list)): raise Exception("keyboard must be a 2d list")
        keyboard = [[str(b) for b in a] for a in keyboard]
        keyboardMarkup = {
            'keyboard': keyboard
        }
        if resize_keyboard: keyboardMarkup['resize_keyboard'] = resize_keyboard
        if one_time_keyboard: keyboardMarkup['one_time_keyboard'] = one_time_keyboard
        if selective: keyboardMarkup['selective'] = selective
        
        self.keyboardMarkup = keyboardMarkup
    
    def default_keyboard_markup(self, selective=None):
        keyboardMarkup = {
            'remove_keyboard': True
        }
        if selective: keyboardMarkup['selective'] = selective
        
        self.keyboardMarkup = keyboardMarkup

    def request(self, method, *args, reply_markup=False, **kwargs):
        if self.keyboardMarkup and reply_markup:
            kwargs['json']['reply_markup'] = self.keyboardMarkup
            self.keyboardMarkup = None
        
        response = requests.get(self.URL + method, *args, **kwargs)
        return response.json()['result']

    def get_updates(self, offset=None, limit=None, timeout=None, allowed_updates=None):
        data = {}
        if offset: data['offset'] = offset
        if offset is None and self.last_update_id is not None: 
            data['offset'] = self.last_update_id
        if limit: data['limit'] = limit
        if timeout: data['timeout'] = timeout
        if allowed_updates: data['allowed_updates'] = allowed_updates
        
        response = self.request('getUpdates', json=data)

        if response:
            self.last_update_id = response[-1]['update_id'] + 1

        return response

    def send_message(self, chat_id, text, parse_mode=None, reply_to_message_id=None):
        data = {
            'chat_id': chat_id,
            'text': text
        }
        if parse_mode: data['parse_mode'] = parse_mode
        if reply_to_message_id: data['reply_to_message_id'] = reply_to_message_id
        
        response = self.request('sendMessage', json=data, reply_markup=True)
        return response

    def edit_message_text(self, chat_id, message_id, text, parse_mode=None):
        data = {
            'chat_id': chat_id,
            'message_id': message_id,
            'text': text
        }
        if parse_mode: data['parse_mode'] = parse_mode

        response = self.request('editMessageText', json=data, reply_markup=True)
        return response

    def send_poll(self, chat_id, question, options, reply_to_message_id=None):
        data = {
            'chat_id': chat_id,
            'question': question,
            'options': options
        }
        if reply_to_message_id: data['reply_to_message_id'] = reply_to_message_id

        response = self.request('sendPoll', json=data, reply_markup=True)
        return response

    def stop_poll(self, chat_id, message_id):
        data = {
            'chat_id': chat_id,
            'message_id': message_id
        }

        response = self.request('stopPoll', json=data, reply_markup=True)
        return response

    def send_photo(self, chat_id, image_path=None, image_url=None, caption=None, parse_mode=None, reply_to_message_id=None):
        data = {
            'chat_id': chat_id
        }
        files = {}
        if image_path: data['photo'] = open(image_path, 'rb')
        if image_url: data['photo'] = image_url
        if caption: data['caption'] = caption
        if parse_mode: data['parse_mode'] = parse_mode
        if reply_to_message_id: data['reply_to_message_id'] = reply_to_message_id
        
        response = self.request('sendPhoto', json=data, files=files, reply_markup=True)
        return response
        