import time
import sensor
import datenbank as db


# speichert die Messwerte alle 60s in der sqlite Datenbank Wetter.db
i = 0
while 1:
	# Messwerte einlesen
	data = sensor.get_data()
	# Messwerte in datenbank speichern
	try:
		db.write_data("Wetter.db", data)
		i = i + 1
		# Ausgeben das Messwerte gespeichert wurden
		print("Es wurden", str(i), "Messreihen durchgeführt.")
	except:
		print("Error")
	time.sleep(60)

