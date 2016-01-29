# Panda2Neo4j

A simple script to insert Pandas DataFrames into Neo4j graphs. There are 2 modes : </br>
<b>Batch Insert : </b> Write nodes and edges to .csv files and call batch insert Py2Neo API </br>
<b>Sequential Insert : </b> Insert node by node, after finishing with nodes, move on inserting edges. </br>

<h3>Sample DataFrame</h3>
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
            
<h3> Imported Graph </h3>
<a href='http://postimg.org/image/t3y1hs4rn/' target='_blank'><img src='http://s13.postimg.org/t3y1hs4rn/Screen_Shot_2016_01_29_at_3_08_27_AM.jpg' border='0' alt="Screen Shot 2016 01 29 at 3 08 27 AM" /></a>

