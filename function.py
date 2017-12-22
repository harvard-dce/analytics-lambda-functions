
import hashlib
from Crypto.Cipher import AES
from os import getenv as env


MD5_LEN = 16
KEYSTRING = env('KEYSTRING')

def handler(event, context):
    pass
