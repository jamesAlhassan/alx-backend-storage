#!/usr/bin/env python3
'''
lists all documents in a collection
'''


def list_all(mongo_collection):
    '''
    arg:mongo_collection
    return: mongo_collection
    '''
    return mongo_collection.find()
