import pyupm_gas as TP401
from AbstractSensor import AbstractSensor
from collections import deque

class AirSensor(AbstractSensor):

	def __init__(self,pin,precision,smoothing=1):
		self.airSensor = TP401.TP401(pin)
		self.precision = precision

		self.smoothing=smoothing
		self.readings=deque(self.smoothing*[0],self.smoothing)

	def readData(self):

		self.readings.append(self.airSensor.getPPM())
		self.data = sum(self.readings)/float(self.smoothing)

		return round(self.data, self.precision)