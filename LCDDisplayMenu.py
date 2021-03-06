from SensorProxy import SensorProxy

class LCDDisplayMenu(object):
	def __init__(self,firstLineEntities,secondLineEntities):
		self.firstLineEntities=firstLineEntities
		self.secondLineEntities=secondLineEntities
		self.firstLine=""
		self.secondLine=""

		self.R=255
		self.G=255
		self.B=255

	def render(self):
		self.firstLine=""
		self.secondLine=""
		for entity in self.firstLineEntities:
			if(isinstance(entity,SensorProxy)):
				self.firstLine+=str(entity.data)
			elif(isinstance(entity,str)):
				self.firstLine+=entity

		for entity in self.secondLineEntities:
			if(isinstance(entity,SensorProxy)):
				self.secondLine+=str(entity.data)
			elif(isinstance(entity,str)):
				self.secondLine+=entity