import json
import hashlib
import hmac
import base64


def generate(options, path, random_string, request=None):
    hash_str = options.base_url + path + options.api_key + options.secret_key + random_string + (
        json.dumps(request) if request else '')
    print(hash_str)
    hashed = hashlib.sha256(hash_str.encode('utf-8')).digest()
    result = base64.b64encode(hashed).decode('utf-8')
    return result


def generate_hash(hash_string):
    hashed = hashlib.sha256(hash_string.encode('utf-8')).hexdigest()
    return hashed


def generate_webhook_signature(cls, merchant_hook_key, hash_string):
    key = merchant_hook_key.encode('utf-8')
    msg = hash_string.encode('utf-8')
    signature = hmac.new(key, msg, hashlib.sha256)
    return base64.b64encode(signature.digest()).decode('utf-8')
