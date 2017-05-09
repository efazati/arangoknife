# Arango Knife
with this lib you can work with arangodb more simpler

there is example to use arangoknife in root project, you can create arangoclass and use it very simple

```
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

```
