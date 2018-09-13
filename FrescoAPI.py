from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table,drop_table
from cassandra.auth import PlainTextAuthProvider
from flask import Flask,jsonify
from models.CustomerSeg import CustomerSeg
from views.api import app

KEYSPACE = "fresco_seg"
auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')


if __name__ == '__main__':
	
	connection.setup(['docker_c_db'],'fresco_seg', protocol_version=3)
	#connection.setup(['10.5.0.5'], "fresco_seg", protocol_version=3)
	sync_table(CustomerSeg)
	#app.run(host="0.0.0.0", port=8081,debug=True,threaded=True,ssl_context=('apicert.pem', 'apikey.pem'))
	app.run(host="0.0.0.0", port=8081,debug=True,threaded=True)

