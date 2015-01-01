#! /usr/bin/env python2
import xml.etree.ElementTree as ET
import sys
import MySQLdb as mdb


def persist(host, user, passw, database, substance, pAc, pIsh, pAs, pUd, effect, under):
	con = mdb.connect(host, user, passw, database, port= 3306)
	with con:
		cur = con.cursor()
		cur.execute('INSERT INTO icd_us_drugs(substance, poisonAcc, poisonIsh, poisonAss, poisonUnd, effect, under) values("'+ substance + '","' + pAc + '","' + pIsh + '","'+ pAs + '","' + pUd + '","'+ effect + '","' + under+ '")')
	if con:
		con.close()


filename = sys.argv[1]
tree = ET.parse(filename)
root = tree.getroot()

for mainterm in root.iter('mainTerm'):
	substance = mainterm.find('title').text
	poisoningAcc1 = ""
	poisoningIsh1 = ""
	poisoningAss1 = ""
	poisoningUndeter1 = ""
	adverseEffect1 = ""
	underdose1 = ""
	print(substance)
	for cell in mainterm.findall('cell'):
		if cell.get('col') == '2':
			poisoningAcc1 = cell.text
		if cell.get('col') == '3':
			poisoningIsh1 = cell.text
		if cell.get('col') == '4':
			poisoningAss1 = cell.text
		if cell.get('col') == '5':
			poisoningUndeter1 = cell.text
		if cell.get('col') == '6':
			adverseEffect1 = cell.text
		if cell.get('col') == '7':
			underdose1 = cell.text
	#Persist to Database	
	if poisoningAcc1 != "" or poisoningIsh1 != "" or poisoningAss1 != "" or poisoningUndeter1 != "" or adverseEffect1 != "" or underdose1 != "":
		persist("138.91.188.176", "tfash", "rqeetub5AFv", "tnaga", substance, poisoningAcc1, poisoningIsh1, poisoningAss1, poisoningUndeter1, adverseEffect1, underdose1)
	for term in mainterm.findall('term'):
		poisoningAcc2 = ""
		poisoningIsh2 = ""
		poisoningAss2 = ""
		poisoningUndeter2 = ""
		adverseEffect2 = ""
		underdose2 = ""
		tit = term.find('title')
		titText = ""
		nem = ""
		if tit != None:
			titText = tit.text
		if tit.find('nemod') != None:
			nem = tit.find('nemod').text
		substance1 = substance + " " + titText + " " + nem
		print(substance1)
		for cell in term.findall('cell'):
			if cell.get('col') == '2':
				poisoningAcc2 = cell.text
			if cell.get('col') == '3':
				poisoningIsh2 = cell.text
			if cell.get('col') == '4':
				poisoningAss2 = cell.text
			if cell.get('col') == '5':
				poisoningUndeter2 = cell.text
			if cell.get('col') == '6':
				adverseEffect2 = cell.text
			if cell.get('col') == '7':
				underdose2 = cell.text
			#Persist to the database
		if poisoningAcc2 != "" or poisoningIsh2 != "" or poisoningAss2 != "" or poisoningUndeter2 != "" or adverseEffect2 != "" or underdose2 != "":
			persist("138.91.188.176", "tfash", "rqeetub5AFv", "tnaga", substance1, poisoningAcc2, poisoningIsh2, poisoningAss2, poisoningUndeter2, adverseEffect2, underdose2)
		for term2 in term.findall('term'):
			poisoningAcc3 = ""
			poisoningIsh3 = ""
			poisoningAss3 = ""
			poisoningUndeter3 = ""
			adverseEffect3 = ""
			underdose3 = ""
			title = term2.find('title')
			titleText = ""
			nemod = ""
			if title != None:
				titleText = title.text
			if title.find('nemod') != None:
				nemod = title.find('nemod').text
			substance2 = substance1 + " " + titleText + " " + nemod
			print(substance2)
			for cell in term2.findall('cell'):
				if cell.get('col') == '2':
					poisoningAcc3 = cell.text
				if cell.get('col') == '3':
					poisoningIsh3 = cell.text
				if cell.get('col') == '4':
					poisoningAss3 = cell.text
				if cell.get('col') == '5':
					poisoningUndete3r = cell.text
				if cell.get('col') == '6':
					adverseEffect3 = cell.text
				if cell.get('col') == '7':
					underdose3 = cell.text
			#Persist to database
			if poisoningAcc3 != "" or poisoningIsh3 != "" or poisoningAss3 != "" or poisoningUndeter3 != "" or adverseEffect3 != "" or underdose3 != "":
				persist("138.91.188.176", "tfash", "rqeetub5AFv", "tnaga", substance2, poisoningAcc3, poisoningIsh3, poisoningAss3, poisoningUndeter3, adverseEffect3, underdose3)
			for term3 in term2.findall('term'):
				poisoningAcc4 = ""
				poisoningIsh4 = ""
				poisoningAss4 = ""
				poisoningUndeter4 = ""
				adverseEffect4 = ""
				underdose4 = ""
				title2 = term3.find('title')
				nemod2 = ""
				title2Text = ""
				if title2 != None:
					title2Text = title2.text
				if title2.find('nemod') != None:
					nemod2 = title2.find('nemod').text
				substance3 = substance2 + " " + title2Text + " " + nemod2
				print(substance3)
				for cell in term3.findall('cell'):
					if cell.get('col') == '2':
						poisoningAcc4 = cell.text
					if cell.get('col') == '3':
						poisoningIsh4 = cell.text
					if cell.get('col') == '4':
						poisoningAss4 = cell.text
					if cell.get('col') == '5':
						poisoningUndeter4 = cell.text
					if cell.get('col') == '6':
						adverseEffect4 = cell.text
					if cell.get('col') == '7':
						underdose4 = cell.text
				#Persist to database
				if poisoningAcc4 != "" or poisoningIsh4 != "" or poisoningAss4 != "" or poisoningUndeter4 != "" or adverseEffect4 != "" or underdose4 != "":
					persist("138.91.188.176", "tfash", "rqeetub5AFv", "tnaga", substance3, poisoningAcc4, poisoningIsh4, poisoningAss4, poisoningUndeter4, adverseEffect4, underdose4)
				for term4 in term3.findall('term'):
					poisoningAcc5 = ""
					poisoningIsh5 = ""
					poisoningAss5 = ""
					poisoningUndeter5 = ""
					adverseEffect5 = ""
					underdose5 = ""
					title3 = term4.find('title')
					nemod3 = ""
					title3Text = ""
					if title3 != None:
						title3Text = title3.text
					if title3.find('nemod') != None:
						nemod3 = title3.find('nemod').text
					substance4 = substance3 + " " + title3Text + " " + nemod3
					print(substance4)
					for cell in term4.findall('cell'):
						if cell.get('col') == '2':
							poisoningAcc = cell.text
						if cell.get('col') == '3':
							poisoningIsh = cell.text
						if cell.get('col') == '4':
							poisoningAss = cell.text
						if cell.get('col') == '5':
							poisoningUndeter = cell.text
						if cell.get('col') == '6':
							adverseEffect = cell.text
						if cell.get('col') == '7':
							underdose = cell.text
					#Persist to database
					if poisoningAcc5 != "" or poisoningIsh5 != "" or poisoningAss5 != "" or poisoningUndeter5 != "" or adverseEffect5 != "" or underdose5 != "":
						persist("138.91.188.176", "tfash", "rqeetub5AFv", "tnaga", substance4, poisoningAcc5, poisoningIsh5, poisoningAss5, poisoningUndeter5, adverseEffect5, underdose5)


