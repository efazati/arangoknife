#!/usr/bin/python
import time
import sys
from pyArango.connection import *
from pyArango.graph import *
from pyArango.collection import *
from pyArango.query import *
from arangoknife import *
from datetime import datetime
import random
import string

class ExampleArango(Arango):
    collection_names = [{'kind':'Collection',
        'name':'vertex'}, 
        {'kind':'Edges',
        'name':'edge'}]
    graph_name = 'example'

    config = {'username': 'efazati',
        'password': "efazati",
        'url': 'http://10.102.1.1:8529',
        'db_conn': "_system"
    }

        
def fill_vertexs():
    arango = ExampleArango()
    start_time = time.time()
    for key in range (1, 1000):
        digits = "".join( [random.choice(string.digits) for i in xrange(8)] )
        chars = "".join( [random.choice(string.letters) for i in xrange(15)] )
        random_name = digits + chars
        each_time = time.time()
        vertex = arango.graph.createVertex('vertex', {"_key": str(key),
            "name": random_name,
            'date': str(datetime.now())});
        vertex.save()
        print 'each time', time.time() - each_time

    print 'all time', time.time() - start_time

def fill_edges():
    arango = ExampleArango()
    query = """FOR doc IN @@collection
      RETURN doc._id"""
    values = {'@collection': 'vertex'}
    result = arango.AQL(query, 1000, values, {}, 1, 1)
    start_time = time.time()
    for item in result:
        from_obj = ArangoDoc(item)
        for i in range(1, 11):
            each_time = time.time()
            to_obj = ArangoDoc('vertex/%s' % random.randint(0,999))
            arango.graph.link('edge', from_obj, to_obj, {'type': 'relation'})
            print 'each time', time.time() - each_time
    print 'all time', time.time() - start_time

if __name__ == "__main__":
    fill_vertexs()
    fill_edges()