import datetime
import plot

# Benutzerdefinierten Plot mit akutellen Einstellung für gewünschtes Datum erstellen
# Datum muss im Format YYYY-mm-dd angegeben sein
# für aktuelles datum str(datetime.datetime.now().strftime("%Y-%m-%d")
# mögliche daten: temperatur, zeit, luftdruck, luftfeuchtigkeit
datum = str("2020-08-28")
print(datum)


def plot_to_folder(date):
	dateiname = "Luftdruck_" + date
	plot.plot("luftdruck", dateiname, date, date)


plot_to_folder(datum)
