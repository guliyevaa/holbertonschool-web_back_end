#!/usr/bin/env python3
# my comment
def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection
    """
    docs = list(mongo_collection.find())
    return docs
