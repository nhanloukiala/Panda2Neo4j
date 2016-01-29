Environment: Python 2.7, Unix, Neo4J 2.2

How to use :

Step 1: Edit the follow configurations in "py2neo4j.py":
serverURL = 'localhost:7474'
dbURL = 'http://localhost:7474/db/data'
account = "neo4j"
password = "conchimnon"

nodename = "Person"
edgename = "RATED"
source_name = "Person"
dest_name = "Person"

Step 2: At root folder, run the following command:

python py2neo4j.py

