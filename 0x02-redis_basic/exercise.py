#!/usr/bin/env python3
'''
0. Writing strings to Redis
'''

import redis


class Cache:
    '''
    Redis Cache Class
    '''

    def __init__(self):
        ' Redis Cache Constructor'
        self._redis = redis.Redis()
        self._redis.flushdb()
