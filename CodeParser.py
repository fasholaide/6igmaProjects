#! /usr/bin/env python2
import sys
import MySQLdb as mdb


def persist(host, user, passw, database, substanceID, substanceCode, desc):
	con = mdb.connect(host, user, passw, database, port= 3306)
	with con:
		cur = con.cursor()
		cur.execute('INSERT INTO icd_10_desc(id, code, description) values("'+ substanceID + '","' + substanceCode + '","' + desc + '")')
	if con:
		con.close()


filename = sys.argv[1]

for line in open(filename):
	substanceID = line[0:5]
	substanceCode = line [5:12]
	substanceCode = substanceCode.strip()
	desc = line [76:]
	if len(substanceCode) > 3:
		substanceCode = substanceCode[:3] + "." + substanceCode[3:]
	print(desc.strip())
	persist("localhost", "root", "tunDEF0958", "TESTDB", substanceID.strip(), substanceCode, desc.strip())

