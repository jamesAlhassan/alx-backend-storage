#!/usr/bin/env python3
'''
0. Writing strings to Redis
'''

import redis
from typing import Union, Optional, Callable
from uuid import uuid4 as uid
from functools import wraps


UnionOfTypes = Union[str, bytes, int, float]


def call_history(method: Callable) -> Callable:
    'stores the history of inputs and outputs for a particular function '
    key = method.__qualname__
    i = "".join([key, ":inputs"])
    o = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        ''''
        add its input parameters to one list in redis, and store its output
        into another list anytime original function is called
        '''
        self._redis.rpush(i, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(o, str(result))
        return result

    return wrapper


def count_calls(method: Callable) -> Callable:
    '''
    a system to count how many
    times methods of the Cache class are called
    '''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
        increments the count for that key every time the
        method is called and returns the value returned by the original
        method.
        '''
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    '''
    Redis Cache Class
    '''

    def __init__(self):
        ' Redis Cache Constructor'
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: UnionOfTypes) -> str:
        '''
        takes a data argument and returns a string.
        The method should generate a random key (e.g. using uuid),
        store the input data in Redis using the random key and
        return the key.
        '''
        key = str(uid())
        self._redis.mset({key: data})

        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> UnionOfTypes:
        'convert the data back to the desired format'
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_int(self: bytes) -> int:
        'get number'
        return int.from_bytes(self, sys.byteorder)

    def get_str(self: bytes) -> str:
        'get  string'
        return self.decode("utf-8")
