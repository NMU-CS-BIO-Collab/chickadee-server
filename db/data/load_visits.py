import mysql.connector as sql
import csv
import sys
import os
import json
import time
import datetime

from itertools import islice
from pprint import *

try:
	visit_data_path = os.getcwd() + "/" + sys.argv[1] + "/"
except IndexError as e:
	print("Visit directory not entered, exiting")
	exit()

config = json.load(open('../../config', 'r'))

cnx = sql.connect(
	user=config["username"],
	password=config["password"],
	database=config["database"]
)

cursor = cnx.cursor(buffered=True)
cnx.get_warnings=True

for f in os.listdir(visit_data_path):
	print("starting " + f)
	feederID = f[:4]
	for line in open(visit_data_path + "/" + f).readlines()[2:]:
		line = line.split(" ")
		rfid = line[0]

		date = str(line[1][:-2]) + "20" + str(line[1][-2:])
		timestamp = date + " " + line[2][:-1]
		timestamp = time.mktime(datetime.datetime.strptime(timestamp, "%m/%d/%Y %H:%M:%S").timetuple())

		command = (
			"INSERT INTO visits (rfid, visitTimestamp, feederID, temperature, mass) "
			"VALUES ('{0}', '{1}', '{2}', 0, 0);".format(rfid, timestamp, feederID))
		cursor.execute(command)

	warnings = cursor.fetchwarnings()
	if warnings: print(warnings)

	print(f + " completed")
print("Visits Loaded")

cursor.close()
cnx.commit()
cnx.close()
