import smbus2
import bme280


# Beschriftung der einzelnen Ausgaben des Sensors BME280
def labels():
	labels = ["Zeit", "Temperatur", "Druck", "Luftfeuchtigkeit"]
	return labels


# Einheiten der einzelnen Ausgaben des Sensors BME280
def units():
	units = [" ", "°C", "hPa", "%"]
	return units


# ließt daten des Sensors BME280 aus und gibt diese als Tuple zurück.
# Runden der Ergebnisse mir r = True auf die n-te Stelle mit acc möglich
def get_data(r=False, acc=12):
	port = 1
	adress = 0x76
	bus = smbus2.SMBus(port)

	calibration_params = bme280.load_calibration_params(bus, adress)
	data = bme280.sample(bus, adress, calibration_params)
	bus.close()
	if r == False:  # Sensoredaten ohne runden
		return data.timestamp, data.temperature, data.pressure, data.humidity
	if r == True:  # Sensoredaten mit runden
		return data.timestamp, round(data.temperature,acc), round(data.pressure,acc), round(data.humidity,acc)

