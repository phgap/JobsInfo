# -*- coding: utf-8 -*-

from pymongo import MongoClient


class Mongodb():
    def __init__(self, ip, port, dbname, collection):
        self.client = MongoClient(ip, port)
        self.db = self.client[dbname]
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
        self.client.close()


if __name__ == "__main__":
    db = mongodb('127.0.0.1', 27017, 'job_info', 'jobs')
