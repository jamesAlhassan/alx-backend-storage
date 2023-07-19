#!/usr/bin/env python3
'''
returns the list of school having a specific topic
mongo_collection will be the pymongo collection object
topic (string) will be topic searched
'''


def schools_by_topic(mongo_collection, topic):
    '''
    args:
        mongo_collection
        topic
    return:
        list of schools
    '''

    return mongo_collection.find({"topic": topic})
