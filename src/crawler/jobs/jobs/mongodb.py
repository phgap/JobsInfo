# -*- coding: utf-8 -*-

from pymongo import MongoClient


class Mongodb():
    def __init__(self, ip, port, dbname, collection):
        client = MongoClient(ip, port)
        self.db = client[dbname]
        self.coll = self.db[collection]

    def save(self, document):
        self.coll.save(document)

    def insert(self, document):
        pass

    def __del__(self, document):
        pass

    def update(self, document):
        pass

    def query(self):
        pass

    def __del__(self):
        pass


if __name__ == "__main__":
    db = mongodb('127.0.0.1', 27017, 'job_info', 'jobs')
