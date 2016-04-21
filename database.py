import sqlite3
import logging
import logging.config
import os
import string





############################################LOGGING###############################################################################################
logging.config.fileConfig('logging_config.ini')
logger = logging.getLogger(os.path.basename(__file__))


############################################FUNCTIONS###############################################################################################
#Connect to Database
def connectDatabase(inputToProcess):
	logger.debug('inputToProcess: %s',inputToProcess)
	
	if inputToProcess:
		logger.debug('inputToProcess is not null or empty')
		conn = sqlite3.connect(inputToProcess)
		return conn
		
		
	else: 
		logger.debug('inputToProcess is null or empty')
		return null
		
		
##Close database		
def closeDatabase(inputToProcess):
	logger.debug('inputToProcess: %s',inputToProcess)
	
	if inputToProcess:
		logger.debug('inputToProcess is not null or empty')
		inputToProcess.close()
		return True
		
	else: 
		logger.debug('inputToProcess is null or empty')
		return False
	
##Commit Database
def commitDatabase(inputToProcess):
	logger.debug('inputToProcess: %s',inputToProcess)
	
	if inputToProcess:
		logger.debug('inputToProcess is not null or empty')
		inputToProcess.commit()
		return True
		
	else: 
		logger.debug('inputToProcess is null or empty')
		return False


##Insert into Table History Price
def insertIntoHistoryPrice(inputDatabaseCursor,inputId,inputLastSellPrice,inputLastRentalPrice,inputUpdateDateTime,inputMyHouseId):
	logger.debug('inputProcess: %s',inputDatabaseCursor)
	logger.debug('inputProcess: %s',inputId)
	logger.debug('inputProcess: %s',inputLastSellPrice)
	logger.debug('inputProcess: %s',inputLastRentalPrice)
	logger.debug('inputProcess: %s',inputUpdateDateTime)
	logger.debug('inputProcess: %s',inputMyHouseId)
	
	try:
		inputDatabaseCursor.execute('''INSERT INTO my_house_history_price_1(id,last_sell_price,last_rental_price,updatedatetime,my_house_id) VALUES(?,?,?,?,?)''',(inputId,inputLastSellPrice,inputLastRentalPrice,inputUpdateDateTime,inputMyHouseId))
		logger.debug('Insert into my house history successfully with id: %s',inputId)
		return True
        
        except ValueError:
			logger.error('ERROR: ID already exists in PRIMARY KEY column {}'.format(inputId))
			return False
		 	


##Insert into Table My House 1 Price
##"id","name","updatedatetime","district","county","city","neighbourhood","streetarea","condition","number_rooms","number_wc","haselevator","floorarea","grossarea","current_sell_price","current_rental_price","notes","htmlpath"
def insertIntoMyHousePrice(inputDatabaseCursor,inputId,inputName,inputUpdatedatetime,inputDistrict,inputCounty,inputCity,inputNeighbourhood,inputStreetarea,inputCondition,inputNumber_rooms,inputNumber_wc,inputHaselevator,inputFloorarea,inputGrossarea,inputCurrent_sell_price,inputCurrent_rental_price,inputNotes,inputHtmlpath):
	logger.debug('inputProcess: %s',inputDatabaseCursor)
	logger.debug('inputProcess: %s',inputId)
	logger.debug('inputProcess: %s',inputName)
	logger.debug('inputProcess: %s',inputUpdatedatetime)
	logger.debug('inputProcess: %s',inputDistrict)
	logger.debug('inputProcess: %s',inputCounty)
	logger.debug('inputProcess: %s',inputCity)
	logger.debug('inputProcess: %s',inputNeighbourhood)
	logger.debug('inputProcess: %s',inputStreetarea)
	logger.debug('inputProcess: %s',inputCondition)
	logger.debug('inputProcess: %s',inputNumber_rooms)
	logger.debug('inputProcess: %s',inputNumber_wc)
	logger.debug('inputProcess: %s',inputHaselevator)
	logger.debug('inputProcess: %s',inputFloorarea)
	logger.debug('inputProcess: %s',inputGrossarea)
	logger.debug('inputProcess: %s',inputCurrent_sell_price)
	logger.debug('inputProcess: %s',inputCurrent_rental_price)
	logger.debug('inputProcess: %s',inputNotes)
	logger.debug('inputProcess: %s',inputHtmlpath)
	
	
	try:
		inputDatabaseCursor.execute('''INSERT INTO my_house_price_1(id,name,updatedatetime,district,county,city,neighbourhood,streetarea,condition,number_rooms,number_wc,haselevator,floorarea,grossarea,current_sell_price,current_rental_price,notes,htmlpath) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(inputId,inputName,inputUpdatedatetime,inputDistrict,inputCounty,inputCity,inputNeighbourhood,inputStreetarea,inputCondition,inputNumber_rooms,inputNumber_wc,inputHaselevator,inputFloorarea,inputGrossarea,inputCurrent_sell_price,inputCurrent_rental_price,inputNotes,inputHtmlpath))
		logger.debug('Insert into my house Price successfully with id: %s',inputId)
		return True
        
        except ValueError exception:
			logger.error('ERROR: ID already exists in PRIMARY KEY column {}'.format(inputId))
			return False
		 	


	
	
