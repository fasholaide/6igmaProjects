#! /usr/bin/env python2
import xml.etree.ElementTree as ET
import sys
import MySQLdb as mdb

def persist(host, user, passw, database, Neo, MalignatPrim, MalignatSec, Ca_in_Situ, Benign, UncertainB, UnspecifiedB):
	con = mdb.connect(host, user, passw, database)
	with con:
		cur = con.cursor()
		cur.execute('INSERT INTO icd_us_neo(Neo, MalignatPrim, MalignatSec, Ca_in_Situ, Benign, UncertainB, UnspecifiedB) values("'+ Neo + '","' + MalignatPrim + '","' + MalignatSec + '","'+ Ca_in_Situ + '","' + Benign + '","'+ UncertainB + '","' + UnspecifiedB + '")')
	if con:
		con.close()


filename = sys.argv[1]
tree = ET.parse(filename)
root = tree.getroot()

for mainterm in root.iter("mainTerm"):
	neoplasm = mainterm.find('title').text
	mailignantPrimary = str()
	malignantSecondary = str()
	ca_in_situ = str()
	benign = str()
	uncertainBehavior = str()
	unspecifiedBehavior = str()
	for cell in mainterm.findall('cell'):
		if cell.get('col') == '2':
			malignantPrimary = cell.text
		if cell.get('col') == '3':
			malignantSecondary = cell.text
		if cell.get('col') == '4':
			ca_in_situ = cell.text
		if cell.get('col') == '5':
			benign = cell.text
		if cell.get('col') == '6':
			uncertainBehavior = cell.text
		if cell.get('col') == '7':
			unspecifiedBehavior = cell.text
	print(neoplasm, malignantPrimary, malignantSecondary, ca_in_situ, benign, uncertainBehavior, unspecifiedBehavior)
	##Persist to database
	if malignantPrimary != "" or malignantSecondary != "" or ca_in_situ != "" or benign != "" or uncertainBehavior != "" or unspecifiedBehavior != "":
		persist('localhost', 'root', 'tunDEF0958', 'TESTDB',neoplasm, malignantPrimary, malignantSecondary, ca_in_situ, benign, uncertainBehavior, unspecifiedBehavior)
	for term in mainterm.findall('term'):
		mailignantPrimary = str()
		malignantSecondary = str()
		ca_in_situ = str()
		benign = str()
		uncertainBehavior = str()
		unspecifiedBehavior = str()
		tit = term.find('title')
		titText = str()
		nem = str()
		if tit != None:
			titText = tit.text
		if tit.find('nemod') != None:
			nem = tit.find('nemod').text
		neoplasm1 = neoplasm.strip() + "|" + titText.strip() + " " + nem
		for cell in term.findall('cell'):
			if cell.get('col') == '2':
				malignantPrimary = cell.text
			if cell.get('col') == '3':
				malignantSecondary = cell.text
			if cell.get('col') == '4':
				ca_in_situ = cell.text
			if cell.get('col') == '5':
				benign = cell.text
			if cell.get('col') == '6':
				uncertainBehavior = cell.text
			if cell.get('col') == '7':
				unspecifiedBehavior = cell.text
		print(neoplasm1, malignantPrimary, malignantSecondary, ca_in_situ, benign, uncertainBehavior, unspecifiedBehavior)
		##Persist to database
		if malignantPrimary != "" or malignantSecondary != "" or ca_in_situ != "" or benign != "" or uncertainBehavior != "" or unspecifiedBehavior != "":
			persist('localhost', 'root', 'tunDEF0958', 'TESTDB',neoplasm1, malignantPrimary, malignantSecondary, ca_in_situ, benign, uncertainBehavior, unspecifiedBehavior)
		for term2 in term.findall('term'):
			mailignantPrimary = str()
			malignantSecondary = str()
			ca_in_situ = str()
			benign = str()
			uncertainBehavior = str()
			unspecifiedBehavior = str()
			tit1 = term2.find('title')
			titText1 = str()
			nem1 = str()
			if tit1 != None:
				titText1 = tit1.text
			if tit1.find('nemod') != None:
				nem1 = tit1.find('nemod').text
			neoplasm2 = neoplasm1.strip() + "|" + titText1.strip() + " " + nem1
			for cell in term2.findall('cell'):
				if cell.get('col') == '2':
					malignantPrimary = cell.text
				if cell.get('col') == '3':
					malignantSecondary = cell.text
				if cell.get('col') == '4':
					ca_in_situ = cell.text
				if cell.get('col') == '5':
					benign = cell.text
				if cell.get('col') == '6':
					uncertainBehavior = cell.text
				if cell.get('col') == '7':
					unspecifiedBehavior = cell.text
			print(neoplasm2, malignantPrimary, malignantSecondary, ca_in_situ, benign, uncertainBehavior, unspecifiedBehavior)
			##Persist to database
			if not titText1.startswith("Note:"):
				if malignantPrimary != "" or malignantSecondary != "" or ca_in_situ != "" or benign != "" or uncertainBehavior != "" or unspecifiedBehavior != "":
					persist('localhost', 'root', 'tunDEF0958', 'TESTDB',neoplasm2, malignantPrimary, malignantSecondary, ca_in_situ, benign, uncertainBehavior, unspecifiedBehavior)
			for term3 in term2.findall('term'):
				mailignantPrimary = str()
				malignantSecondary = str()
				ca_in_situ = str()
				benign = str()
				uncertainBehavior = str()
				unspecifiedBehavior = str()
				tit2 = term3.find('title')
				titText2 = str()
				nem2 = str()
				if tit2 != None:
					titText2 = tit2.text
				if tit2.find('nemod') != None:
					nem2 = tit2.find('nemod').text
				neoplasm3 = neoplasm2.strip() + "|" + titText2.strip() + " " + nem2
				for cell in term3.findall('cell'):
					if cell.get('col') == '2':
						malignantPrimary = cell.text
					if cell.get('col') == '3':
						malignantSecondary = cell.text
					if cell.get('col') == '4':
						ca_in_situ = cell.text
					if cell.get('col') == '5':
						benign = cell.text
					if cell.get('col') == '6':
						uncertainBehavior = cell.text
					if cell.get('col') == '7':
						unspecifiedBehavior = cell.text
				print(neoplasm3, malignantPrimary, malignantSecondary, ca_in_situ, benign, uncertainBehavior, unspecifiedBehavior)
				##Persist to database
				if malignantPrimary != "" or malignantSecondary != "" or ca_in_situ != "" or benign != "" or uncertainBehavior != "" or unspecifiedBehavior != "":
					persist('localhost', 'root', 'tunDEF0958', 'TESTDB',neoplasm3, malignantPrimary, malignantSecondary, ca_in_situ, benign, uncertainBehavior, unspecifiedBehavior)
				for term4 in term3.findall('term'):
					mailignantPrimary = str()
					malignantSecondary = str()
					ca_in_situ = str()
					benign = str()
					uncertainBehavior = str()
					unspecifiedBehavior = str()
					tit3 = term4.find('title')
					titText3 = str()
					nem3 = str()
					if tit3 != None:
						titText3 = tit3.text
					if tit3.find('nemod') != None:
						nem3 = tit3.find('nemod').text
					neoplasm4 = neoplasm3.strip() + "|" + titText3.strip() + " " + nem3
					for cell in term4.findall('cell'):
						if cell.get('col') == '2':
							malignantPrimary = cell.text
						if cell.get('col') == '3':
							malignantSecondary = cell.text
						if cell.get('col') == '4':
							ca_in_situ = cell.text
						if cell.get('col') == '5':
							benign = cell.text
						if cell.get('col') == '6':
							uncertainBehavior = cell.text
						if cell.get('col') == '7':
							unspecifiedBehavior = cell.text
					print(neoplasm4, malignantPrimary, malignantSecondary, ca_in_situ, benign, uncertainBehavior, unspecifiedBehavior)
					##Persist to database
					if malignantPrimary != "" or malignantSecondary != "" or ca_in_situ != "" or benign != "" or uncertainBehavior != "" or unspecifiedBehavior != "":
						persist('localhost', 'root', 'tunDEF0958', 'TESTDB',neoplasm4, malignantPrimary, malignantSecondary, ca_in_situ, benign, uncertainBehavior, unspecifiedBehavior)
