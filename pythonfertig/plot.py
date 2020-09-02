import matplotlib
import datetime
import datenbank as db
import matplotlib.pyplot as plt
from matplotlib import dates


# Bsp: plot("luftfeuchtigkeit", "luftfeuchtigkeit10.png", "2020-08-26", "2020-08-26")
# Plottet eine bestimmte spalten (y_value) der db gegen die Zeit.
def plot(y_value, name, startdate, enddate):  # dates in "yyyy-mm-dd"
    sdate = datetime.datetime.strptime(startdate, "%Y-%m-%d").date()
    edate = datetime.datetime.strptime(enddate, "%Y-%m-%d").date()
    delta = edate - sdate
    datelist = []

    for i in range(delta.days + 1):
        day = sdate + datetime.timedelta(days=i)
        datelist.append(day)

    y_value = y_value.lower()
    time = []
    y_axis = []
    for date in datelist:
        time += db.read_data("Wetter.db", '"' + str(date) + '"', "zeit")
        y_axis += db.read_data("Wetter.db", '"' + str(date) + '"', y_value)

    # wende auf jeden eintrag in time strptime an, um es danach formatieren zu können
    x_axis = list(map(datetime.datetime.strptime, time, len(time) * ['%Y-%m-%d %H:%M:%S.%f']))

    fig, ax = plt.subplots()
    # aussehen der Ticks zu HH:MM ändern und in formatter speichern
    formatter = dates.DateFormatter("%H:%M")
    # formatter auf x-achse anwenden, sodass die Ticks labels der Form HH:MM haben
    ax.xaxis.set_major_formatter(formatter)

    # Plot title hinzufügen
    if not enddate == startdate:
        title = y_value.capitalize() + " vom " + startdate + " bis zum " + enddate
    else:
        title = y_value.capitalize() + " vom " + startdate
    # Richtige Einheiten, Achsenbeschriftung und Achsenskalierung in Abhängigkeit von der gewählten Spalte
    if y_value == "temperatur":
        ylabel = "Temperatur in °C"
        minvalue = 15
        maxvalue = 30
    elif y_value == "luftfeuchtigkeit":
        ylabel = "Luftfeuchtigkeit in %"
        minvalue = 40
        maxvalue = 100
    elif y_value == "luftdruck":
        ylabel = "Druck in hPa"
        minvalue = 900
        maxvalue = 1100
    # plot_date zum Plotten von Daten, xdate = True, da Daten auf x-Achse. Punkte mit ms=1 verkleinert.
    ax.plot_date(x_axis, y_axis, '.', ms=1, xdate=True)
    # Achsenskalierung setzten
    ax.set_ylim(minvalue, maxvalue)
    # rotieren der Daten auf der x-Achse um 45 Grad siehe https://matplotlib.org/3.3.1/gallery/recipes/common_date_problems.html
    fig.autofmt_xdate()
    ax.set_ylabel(ylabel)
    plt.title(title)
    # Plot im ordner static/plots/ speichern, damit der Webserver darauf zugreifen kann.
    fig.savefig("./pythonweb/static/plots/" + name + ".jpg")
    plt.close()





