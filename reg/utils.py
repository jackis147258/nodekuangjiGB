# utils.py

from .messages import messages

def get_message(lang, key):
    return messages.get(lang, {}).get(key, key)
