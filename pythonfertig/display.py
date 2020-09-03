from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
import time
import sensor

# Display einrichten
serial = i2c(port=1, address=0x3C)
device = sh1106(serial)


# Display Ausgabe von aktuellen Sensordaten mit Einheiten und verschiebung der y Position des Textes
while 1:
    for i, j, k, l in zip(sensor.get_data(r=True, acc=2), sensor.labels(), sensor.units(), [0, 1, 2, 3]):
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            draw.text((10, l*10+5), j + "\n" + str(i) + " " + k, fill="white")
        time.sleep(3)
