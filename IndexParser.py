# /usr/bin/env python2
##It has nine layers
import xml.etree.ElementTree as ET
import sys
import MySQLdb as mdb

def persist(host, user, passw, database, term, code):
	con = mdb.connect(host, user, passw, database)
	with con:
		cur = con.cursor()
		cur.execute('INSERT INTO icd_us_neo(term, code) values("'+ term + '","' + code + '")')
	if con:
		con.close()


filename = sys.argv[1]
tree = ET.parse(filename)
root = tree.getroot()

##It has nine layers
for mainterm in root.iter('mainTerm'):
	inj_dis_temp = mainterm.find('title')
	code_temp = mainterm.find('code')
	nem = str()
	inj_dis = str()
	code = str()
	if inj_dis_temp.find('nemod') != None:
		nem = inj_dis_temp.find('nemod').text.strip()
	if inj_dis_temp != None:
		inj_dis = inj_dis_temp.text.strip()+ " " + nem
	if code_temp != None:
		code = code_temp.text.strip()
	if inj_dis != "" and code != "":
		print(inj_dis)
		persist('localhost', 'root', 'tunDEF0958', 'TESTDB', inj_dis.strip(), code)
	for term1 in mainterm.findall('term'):
		inj_dis_temp1 = term1.find('title')
		code_temp1 = term1.find('code')
		code = str()
		nem = str()
		inj_dis1 = str()
		if inj_dis_temp1.find('nemod') != None:
			nem = inj_dis_temp1.find('nemod').text.strip()
		if inj_dis_temp1 != None:
			inj_dis1 = inj_dis + "|" +inj_dis_temp1.text.strip() + " " + nem
		if code_temp1 != None:
			code = code_temp1.text.strip()
		if inj_dis1 != "" and code != "":
			print(inj_dis1)
			persist('localhost', 'root', 'tunDEF0958', 'TESTDB', inj_dis1.strip(), code)
		for term2 in term1.findall('term'):
			inj_dis_temp2 = term2.find('title')
			code_temp2 = term2.find('code')
			code = str()
			nem = str()
			inj_dis2 = str()
			if inj_dis_temp2.find('nemod') != None:
				nem = inj_dis_temp2.find('nemod').text.strip()
			if inj_dis_temp2 != None:
				inj_dis2 = inj_dis1 + "|" +inj_dis_temp2.text.strip() + " " + nem
			if code_temp2 != None:
				code = code_temp2.text.strip()
			if inj_dis2 != "" and code != "":
				print(inj_dis2)
				persist('localhost', 'root', 'tunDEF0958', 'TESTDB', inj_dis2.strip(), code)
			for term3 in term2.findall('term'):
				inj_dis_temp3 = term3.find('title')
				code_temp3 = term3.find('code')
				code = str()
				nem = str()
				inj_dis3 = str()
				if inj_dis_temp3.find('nemod') != None:
					nem = inj_dis_temp3.find('nemod').text.strip()
				if inj_dis_temp3 != None:
					inj_dis3 = inj_dis2 + "|" +inj_dis_temp3.text.strip() + " " + nem
				if code_temp3 != None:
					code = code_temp3.text.strip()
				if inj_dis3 != "" and code != "":
					print(inj_dis3)
					persist('localhost', 'root', 'tunDEF0958', 'TESTDB', inj_dis3.strip(), code)
				for term4 in term3.findall('term'):
					inj_dis_temp4 = term4.find('title')
					code_temp4 = term4.find('code')
					code = str()
					nem = str()
					inj_dis4 = str()
					if inj_dis_temp4.find('nemod') != None:
						nem = inj_dis_temp4.find('nemod').text.strip()
					if inj_dis_temp4 != None:
						inj_dis4 = inj_dis3 + "|" +inj_dis_temp4.text.strip() + " " + nem
					if code_temp4 != None:
						code = code_temp4.text.strip()
					if inj_dis4 != "" and code != "":
						print(inj_dis4)
						persist('localhost', 'root', 'tunDEF0958', 'TESTDB', inj_dis4.strip(), code)
					for term5 in term4.findall('term'):
						inj_dis_temp5 = term5.find('title')
						code_temp5 = term5.find('code')
						code = str()
						nem = str()
						inj_dis5 = str()
						if inj_dis_temp5.find('nemod') != None:
							nem = inj_dis_temp5.find('nemod').text.strip()
						if inj_dis_temp5 != None:
							inj_dis5 = inj_dis4 + "|" +inj_dis_temp5.text.strip() + " " + nem
						if code_temp5 != None:
							code = code_temp5.text.strip()
						if inj_dis5 != "" and code != "":
							print(inj_dis5)
							persist('localhost', 'root', 'tunDEF0958', 'TESTDB', inj_dis5.strip(), code)
						for term6 in term5.findall('term'):
							inj_dis_temp6 = term6.find('title')
							code_temp6 = term6.find('code')
							code = str()
							nem = str()
							inj_dis6 = str()
							if inj_dis_temp6.find('nemod') != None:
								nem = inj_dis_temp6.find('nemod').text.strip()
							if inj_dis_temp6 != None:
								inj_dis6 = inj_dis5 + "|" +inj_dis_temp6.text.strip() + " " + nem
							if code_temp6 != None:
								code = code_temp6.text.strip()
							if inj_dis6 != "" and code != "":
								print(inj_dis6)
								persist('localhost', 'root', 'tunDEF0958', 'TESTDB', inj_dis6.strip(), code)
							for term7 in term6.findall('term'):
								inj_dis_temp7 = term7.find('title')
								code_temp7 = term7.find('code')
								code = str()
								nem = str()
								inj_dis7 = str()
								if inj_dis_temp7.find('nemod') != None:
									nem = inj_dis_temp7.find('nemod').text.strip()
								if inj_dis_temp7 != None:
									inj_dis7 = inj_dis6 + "|" +inj_dis_temp7.text.strip() + " " + nem
								if code_temp7 != None:
									code = code_temp7.text.strip()
								if inj_dis7 != "" and code != "":
									print(inj_dis7)
									persist('localhost', 'root', 'tunDEF0958', 'TESTDB', inj_dis7.strip(), code)
								for term8 in term7.findall('term'):
									inj_dis_temp8 = term8.find('title')
									code_temp8 = term8.find('code')
									code = str()
									nem = str()
									inj_dis8 = str()
									if inj_dis_temp8.find('nemod') != None:
										nem = inj_dis_temp8.find('nemod').text.strip()
									if inj_dis_temp8 != None:
										inj_dis8 = inj_dis7 + "|" +inj_dis_temp8.text.strip() + " " + nem
									if code_temp8 != None:
										code = code_temp8.text.strip()
									if inj_dis8 != "" and code != "":
										print(inj_dis8)
										persist('localhost', 'root', 'tunDEF0958', 'TESTDB', inj_dis8.strip(), code)
									for term9 in term8.findall('term'):
										inj_dis_temp9 = term9.find('title')
										code_temp9 = term9.find('code')
										code = str()
										nem = str()
										inj_dis9 = str()
										if inj_dis_temp9.find('nemod') != None:
											nem = inj_dis_temp9.find('nemod').text.strip()
										if inj_dis_temp9 != None:
											inj_dis9 = inj_dis8 + "|" +inj_dis_temp9.text.strip() + " " + nem
										if code_temp9 != None:
											code = code_temp9.text.strip()
										if inj_dis9 != "" and code != "":
											print(inj_dis9)
											persist('localhost', 'root', 'tunDEF0958', 'TESTDB', inj_dis9.strip(), code)
