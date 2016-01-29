__author__ = 'nhan'
import pandas as pd
import os
import importlib
import urlparse, urllib

def checkDependency():
    try:
        import py2neo
    except:
        import pip
        pip.main(['install', 'py2neo'])

checkDependency()
from py2neo import Graph, authenticate, Node, Relationship

nodedata = [{'subid': '1', 'age': 75, 'fdg': 1.78, 'name': 'Mike'},
            {'subid': '2', 'age': 33, 'fdg': 1.56, 'name': 'June'},
            {'subid': '3', 'age': 32, 'fdg': 1.11, 'name': 'Jane'},
            {'subid': '4', 'age': 77, 'fdg': 1.02, 'name': 'Fred'},
            {'subid': '5', 'age': 26, 'fdg': 4.33, 'name': 'Alex'},
            {'subid': '6', 'age': 54, 'fdg': 2.11, 'name': 'Thom'},
            {'subid': '7', 'age': 24, 'fdg': 5.22, 'name': 'Codu'}]
nodes = pd.DataFrame(nodedata)

edgedata = [{'source': '1', 'dest': '2', 'weight': 1, 'rating': 2},
            {'source': '1', 'dest': '3', 'weight': 1, 'rating': 1},
            {'source': '1', 'dest': '5', 'weight': 1, 'rating': 6},
            {'source': '1', 'dest': '6', 'weight': 1, 'rating': 8},
            {'source': '6', 'dest': '7', 'weight': 1, 'rating': 3},
            {'source': '5', 'dest': '3', 'weight': 1, 'rating': 4},
            {'source': '4', 'dest': '3', 'weight': 1, 'rating': 9},
            {'source': '2', 'dest': '4', 'weight': 1, 'rating': 2}]
edges = pd.DataFrame(edgedata)

#create paths
currentFolder = os.getcwd() + os.sep
nodePath = currentFolder + 'nodes.csv'
edgePath = currentFolder + 'edges.csv'

#write csv to paths
nodes.to_csv(nodePath, index=False)
edges.to_csv(edgePath, index=False)

#config params
serverURL = 'localhost:7474'
dbURL = 'http://localhost:7474/db/data'
account = "neo4j"
password = "conchimnon"

#connect to DB
authenticate(serverURL, user_name=account, password=password)
graph = Graph(dbURL)

#get os file URI
def path2url(path):
    return urlparse.urljoin('file:', urllib.pathname2url(path))

#cypher params
nodename = "Person"
edgename = "RATED"
source_name = "Person"
dest_name = "Person"

#BATCH IMPORT TO NEO4J FROM CSV FILE
#import node
graph.cypher.execute("LOAD CSV WITH HEADERS FROM '%s' AS csvLine " % (path2url(nodePath)) +
                     " CREATE (p:"+nodename+" { id: toInt(csvLine.subid), name: csvLine.name, age: toInt(csvLine.age), fdg: toFloat(csvLine.fdg) })")

#import edges
tx = graph.cypher.begin()
statement = "USING PERIODIC COMMIT 500" \
            + " LOAD CSV WITH HEADERS FROM '" + path2url(edgePath) + "' AS csvLine" \
            + " MATCH (person:"+source_name+" { id: toInt(csvLine.source)}),(person1:"+dest_name+" { id: toInt(csvLine.dest)})" \
            + " CREATE (person)-[:"+edgename+" { rating: toInt(csvLine.rating), weight: toInt(csvLine.weight) }]->(person1)"
tx.append(statement)
tx.commit()

#NODE BY NODE IMPORT
for index, row in nodes.iterrows():
    node = Node(nodename, id=int(row['subid']), age = row['age'], fdg = row['fdg'], name = row['name'])
    graph.create(node)

for index, row in edges.iterrows():
    source_node = graph.find_one(nodename, property_key='id', property_value=int(row['source']))
    dest_node = graph.find_one(nodename, property_key='id', property_value = int(row['dest']))
    relation = Relationship(source_node, edgename, dest_node, rating = int(row['rating']))
    graph.create(relation)
