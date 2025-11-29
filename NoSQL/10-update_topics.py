#!/usr/bin/env python3
""" Update topics of a school document """
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
    Args:
        mongo_collection: pymongo collection object
        name (string): school name to update
        topics (list of strings): new list of topics
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
