# Panda2Neo4j

A simple script to insert Pandas DataFrames into Neo4j graphs. There are 2 modes : </br></br>
<b>Batch Insert : </b> Write nodes and edges to .csv files and call batch insert Py2Neo API </br>
<b>Sequential Insert : </b> Insert node by node, after finishing with nodes, move on inserting edges. </br>

Environment: Python 2.7, Unix, Neo4J 2.2 </br>

How to use : </br>

Step 1: Edit the follow configurations in "py2neo4j.py": </br>
serverURL = 'localhost:7474' </br>
dbURL = 'http://localhost:7474/db/data'</br> 
account = "neo4j"</br> 
password = "conchimnon"</br>
</br>
nodename = "Person"</br>
edgename = "RATED"</br>
source_name = "Person"</br>
dest_name = "Person"</br></br>

Step 2: At root folder, run the following command:</br></br>

<blockquote>python py2neo4j.py</blockquote>
