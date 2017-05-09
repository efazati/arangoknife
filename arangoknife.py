#!/usr/bin/python
import sys
from pyArango.connection import *
from pyArango.graph import *
from pyArango.collection import *
from pyArango.query import *


# config = 

class Arango(object):
    collection_names = []
    graph_name = ''

    config = {'username': 'user',
        'password': "pass",
        'url': 'http://127.0.0.1:8529',
        'db_conn': "_system"
    }

    def __init__(self):
        self.db = self.get_db()
        for col in self.collection_names:
            setattr(self, col['name'], self.get_collection(col))
        
        if self.graph_name:
            self.graph = self.get_graph(self.graph_name)

    def get_db(self):
        conn = Connection(arangoURL=self.config['url'], 
            username=self.config['username'], password=self.config['password'])
        db = conn[self.config['db_conn']]
        return db

    def get_collection(self, obj):
        if not self.db.hasCollection(obj['name']):
            col = self.db.createCollection(obj['kind'], name=obj['name'])
        else:
            col = self.db.collections[obj['name']]

        return col

    def get_graph(self, name):
        if not self.db.hasGraph(name):
            g = self.db.createGraph(name)
        else:
            g = self.db.graphs[name]
        return g

    def AQL(self, *args, **kwargs):
        return AQLQuery(self.db, *args, **kwargs)
        

class ArangoDoc(object):
    def __init__(self, id):
        self._id = id