from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.auth import PlainTextAuthProvider
from flask import Flask,jsonify
from models.CustomerSeg import CustomerSeg
from views.api import app
#from sync_db import sync_db

KEYSPACE = "fresco_seg"

auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')

#cluster = Cluster(['10.5.0.5'], auth_provider=auth_provider, protocol_version=2)
#session = cluster.connect(keyspace=KEYSPACE)


#session = cluster.connect()
# session.execute(
 # """
        # CREATE KEYSPACE IF NOT EXISTS %s WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
        # """ % KEYSPACE)


#    return app


#app = create_app()
#api = Api(app)

if __name__ == '__main__':
    connection.setup(['10.5.0.5'], "fresco_seg", protocol_version=3)
    sync_table(CustomerSeg)
    app.run(host="0.0.0.0", port=8081,debug=True)
