import hashlib
import json


def hash_string(string):
    return hashlib.sha256(string).hexdigest()


def hash_block(block):
    """ hashes a block and returns representation of block """

    # hashing blocks, conversion to formated string, encoding
    # hexdigest method returns hash with normal characters
    return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()