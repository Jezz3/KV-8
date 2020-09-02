import plot
import datetime
import time


def update_website(date):
    # Temperatur in HTML Code der Website einfügen
    # öffnen der HTML datei und Zeilen in liste einlesen, Datei wieder schließen
    datei = open("./pythonweb/templates/index1.html", "r")
    data = datei.readlines()
    datei.close()
    # liste mit neuem Codezeilen als einzelne Elemente der Liste erstellen
    new_data = ['<div class="w3-third">\n',
                '<h3>{}</h3>\n'.format(date),
                ' <div class="w3-animate-zoom">\n',
                '  <div class="zoom">\n',
                '    <img src="/static/plots/Temperatur_{}.jpg" alt="{}" style="width:100%;max-width:90%">\n'.format(date, date),
                '  </div>\n',
                ' </div>\n',
                '</div>\n',
                '\n']
    # Liste mit eigelesenen Zeilen an der stellen, wo die neuen Zeilen eingefügt werden sollen(43) splitten und
    # neue Zeilen dazwischen hinzufügen.
    combined_data = data[:52] + new_data + data[52:]
    # mit der neuen Liste die alten Zeilen der Datei überschreiben
    datei = open("./pythonweb/templates/index1.html", "w")
    datei.writelines(combined_data)
    datei.close()


# Luftfeuchtigkeit in HTML Code der Website einfügen


def plot_to_folder(date):
    # plot der vorhandenen Daten in der db für ein Datum erstellen
    # Wenn read_data aufgerufen wird bevor einmal write_data aufgerufen wurde exisitert die db noch nicht
    # Deswegen try und except, sodass das Programm nicht durch den Fehler stehenbleibt.
    try:
        dateiname = "Temperatur_" + date
        plot.plot("temperatur", dateiname, date, date)
    except OperationalError:  # Fehler das Datenbank noch nicht existiert abfangen
        print("sqlite3.OperationalError am ", str(date))
    except:
        print("Weitere Fehler am: " + str(date))


# Website und Plot beim ersten ausführen der Datei aktualisieren
date = str(datetime.datetime.now().strftime("%Y-%m-%d"))
uhrzeit = str(datetime.datetime.now().strftime("%H:%M"))
plot_to_folder(date)
update_website(date)
print("Website und Plot wurde um " + uhrzeit + " aktualisiert")

# Plot alle 60 Sekunden neu erstellen, die Website zeigt dann beim erneuten Aufruf die neue Plot Datei an
while 1:
    date = str(datetime.datetime.now().strftime("%Y-%m-%d"))
    uhrzeit = str(datetime.datetime.now().strftime("%H:%M"))
    time.sleep(60)
    dateNeu = str(datetime.datetime.now().strftime("%Y-%m-%d"))
    plot_to_folder(dateNeu)
    # Datum alle 60s vergleichen. Um 00:00 sie die Daten nicht gleich, dann Website aktualisieren,
    # indem über update_website, der HTML Code für den Plot des nächsten Tages eingefügt wird
    if date != dateNeu:
        update_website(dateNeu)
        print("Website wurde um " + uhrzeit + " aktualisiert")
    print("Der Plot wurde um " + uhrzeit + " aktualisiert")
