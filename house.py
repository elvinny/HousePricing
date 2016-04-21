import logging
import logging.config
import os


############################################LOGGING###############################################################################################
logging.config.fileConfig('logging_config.ini')
logger = logging.getLogger(os.path.basename(__file__))

############################################CLASS###############################################################################################

class House(object):
	
	@property
	def get_name(self):
		logger.debug('Get name : %s',self.name)
		return self.name
	
	@property
	def get_updatedatetime(self):
		logger.debug('Get Update date time : %s',self.updatedatetime)
		return self.updatedatetime
			
	@property
	def get_district(self):
		logger.debug('Get District : %s',self.district)
		return self.district
			
	@property
	def get_county(self):
		logger.debug('Get County : %s',self.county)
		return self.county
		
	@property
	def get_city(self):
		logger.debug('Get City : %s',self.city)
		return self.city
		
	@property
	def get_neighbourhood(self):
		logger.debug('Get Neighbourhood : %s',self.neighbourhood)
		return self.neighbourhood
		
	@property
	def get_streetarea(self):
		logger.debug('Get Street Area : %s',self.streetarea)
		return self.streetarea
	 
	@property
	def get_condition(self):
		logger.debug('Get Condition : %s',self.condition)
		return self.condition
		
	@property
	def get_number_rooms(self):
		logger.debug('Get Number of Rooms : %s',self.number_rooms)
		return self.number_rooms
		
	@property
	def get_number_wc(self):
		logger.debug('Get Number of WCs : %s',self.number_wc)
		return self.number_wc
		
	@property
	def get_getHasElevator(self):
		logger.debug('Get Has Elevator : %s',self.haselevator)
		return (self.haselevator)

	@property
	def get_floorarea(self):
		logger.debug('Get Floor Area : %s',self.floorarea)
		return self.floorarea
		
	@property
	def get_grossarea(self):
		logger.debug('Get Gross Area : %s',self.grossarea)
		return self.grossarea
		
	@property
	def get_current_sell_price(self):
		logger.debug('Get Current Sell Price : %s',self.current_sell_price)
		return (self.current_sell_price)
		
	@property	
	def get_current_rental_price_price(self):
		logger.debug('Get Current Rental Price : %s',self.current_rental_price_price)
		return (self.current_rental_price_price)
		
	@property
	def get_last100_sell_price(self):
		logger.debug('Get Last 100 Sell Price : %s',self.last100_sell_price)
		return (self.last100_sell_price)   
		
	@property
	def get_last100_rental_price(self):
		logger.debug('Get Last 100 Rental Price : %s',self.last100_rental_price)
		return (self.last100_rental_price)   
		
	@property
	def get_notes(self):
		logger.debug('Get Notes : %s',self.notes)
		return (self.notes) 
		
	@property
	def get_htmlpath(self):
		logger.debug('Get HTML Path : %s',self.htmlpath)
		return (self.htmlpath)   

	
	def name(self,value):
		logger.debug('Setting name with value : %s',value)
		self.name = value
		
	
	def updatedatetime(self,value):
		logger.debug('Setting updatedatetime with value : %s',value)
		self.updatedatetime = value	
			
	
	def district(self,value):
		logger.debug('Setting district with value : %s',value)
		self.district = value
		
		
	
	def county(self,value):
		logger.debug('Setting county with value : %s',value)
		self.county = value
			
	
	def city(self,value):
		logger.debug('Setting county with value : %s',value)
		self.county = value
		

	
	def neighbourhood(self,value):
		logger.debug('Setting neighbourhood with value : %s',value)
		self.neighbourhood = value
		
		
	
	def streetarea(self,value):
		logger.debug('Setting streetarea with value : %s',value)
		self.streetarea = value
		
	
	def condition(self,value):
		logger.debug('Setting condition with value : %s',value)
		self.condition = value
	 
		
	
	def number_rooms(self,value):
		logger.debug('Setting number_rooms with value : %s',value)
		self.number_rooms = value
		

	
	def number_wc(self,value):
		logger.debug('Setting number_wc with value : %s',value)
		self.number_wc = value


	
	def haselevator(self,value):
		logger.debug('Setting haselevator with value : %s',value)
		self.haselevator = value	
		
		
	
	def floorarea(self,value):
		logger.debug('Setting floorarea with value : %s',value)
		self.floorarea = value	
		
	
	def grossarea(self,value):
		logger.debug('Setting grossarea with value : %s',value)
		self.grossarea = value	
			
	
	def current_sell_price(self,value):
		logger.debug('Setting current_sell_price with value : %s',value)
		self.current_sell_price = value	

	
	def current_rental_price(self,value):
		logger.debug('Setting current_rental_price with value : %s',value)
		self.current_rental_price = value	
		
		
	
	def last100_sell_price(self,value):
		logger.debug('Setting last100_sell_price with value : %s',value)
		self.last100_sell_price = value	
		
	
	def last100_rental_price(self,value):
		logger.debug('Setting last100_rental_price with value : %s',value)
		self.last100_rental_price = value	
		
	
	def notes(self,value):
		logger.debug('Setting notes with value : %s',value)
		self.notes = value	
		
	
	def htmlpath(self,value):
		logger.debug('Setting htmlpath with value : %s',value)
		self.htmlpath = value	
	
		
	def __init__(self,name,updatedatetime,district,
	county,city,neighbourhood,streetarea,condition,number_rooms,
	number_wc,haselevator,floorarea,grossarea,current_sell_price,
	current_rental_price,last100_sell_price,last100_rental_price,notes,htmlpath):
		self.name = name
		self.updatedatetime = updatedatetime
		self.district = district
		self.county = county
		self.city = city
		self.neighbourhood = neighbourhood
		self.streetarea = streetarea
		self.condition = condition
		self.number_rooms = number_rooms
		self.number_wc = number_wc
		self.haselevator = haselevator
		self.floorarea = floorarea
		self.grossarea = grossarea
		self.current_sell_price = current_sell_price
		self.current_rental_price = current_rental_price
		self.last100_sell_price = last100_sell_price
		self.last100_rental_price = last100_rental_price
		self.notes = notes
		self.htmlpath = htmlpath
			
############################################FUNCTION GET###############################################################################################
		
		
	
	
