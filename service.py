#!/usr/bin/python3

import json
import sqlite3
import http.server
import socketserver

PORT = 8000

def registrerAvvik(avvik):
	try:
		conn = sqlite3.connect("avvik.db")
		cur = conn.cursor()
		cur.execute("INSERT INTO Avvik ('plukkdato', 'plukknr', 'lokasjon', 'feiltype') values (?, ?, ?, ?)", (avvik['plukkdato'], avvik['plukknr'], avvik['lokasjon'], avvik['feilType']))
		conn.commit()
		conn.close()
		print("Avviket ble lagret i databasen.")
	except BaseException as err:
		if str(err) == "no such table: Avvik":
			print("Tabellen finnes ikke i databasefilen; oppretter den og prøver igjen...")
			cur.execute(
				"""
				CREATE TABLE IF NOT EXISTS "Avvik" (
			        "Id"            INTEGER,
			        "plukkdato"     DATE,
			        "plukknr"       INTEGER,
			        "lokasjon"      TEXT,
			        "feiltype"      TEXT,
			        "tidspunkt"     DATETIME DEFAULT CURRENT_TIMESTAMP,
			        PRIMARY KEY("Id" AUTOINCREMENT)
				);
				""")
			registrerAvvik(avvik);
		else:
			print(f"Kunne ikke lagre avvik i DB: {err}, {type(err)}")

class MyHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		super().do_GET()
	def do_POST(self):
		content_len = int(self.headers.get('Content-Length'))
		content = self.rfile.read(content_len).decode('utf-8')
		print("Mottok HTTP POST-body: " + content)
		avvik = json.loads(content)
		print("Python JSON-object: ", avvik)
		registrerAvvik(avvik)
		self.send_response(200)
		self.end_headers()
		self.wfile.write(b'OK')

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
	print("HTTP-Server lytter nå på port", PORT)
	httpd.serve_forever()
