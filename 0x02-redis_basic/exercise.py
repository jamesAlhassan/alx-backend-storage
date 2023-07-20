#!/usr/bin/env python3
'''
0. Writing strings to Redis
'''

import redis
from typing import Union
from uuid import uuid4 as uid


UnionOfTypes = Union[str, bytes, int, float]


class Cache:
    '''
    Redis Cache Class
    '''

    def __init__(self):
        ' Redis Cache Constructor'
        self._redis = redis.Redis()
        self._redis.flushdb()

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
