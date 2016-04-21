from datetime import datetime
import logging
import logging.config
import os
import unicodedata
import string
import re




############################################LOGGING###############################################################################################
logging.config.fileConfig('logging_config.ini')
logger = logging.getLogger(os.path.basename(__file__))


############################################FUNCTIONS###############################################################################################
## REMOVE STRANGE CHARs
def removeStrangeChars(inputToProcess):
	logger.debug('#############################################START REMOVESTRANGECHARS#############################################')
	
	logger.debug('inputToProcess: %s',inputToProcess)
	
	result = ''.join(e for e in inputToProcess if e.isalnum())
	
	logger.debug('result: %s',result)
	
	logger.debug('#############################################END REMOVESTRANGECHARS#############################################')
	
	return result
		
## REMOVE ACCENTS FROM STRINGS	
def remove_accents(data):
    return ''.join(x for x in unicodedata.normalize('NFKD', data) if x in string.ascii_letters).lower()


## REMOVE ALL ALPHABET FROM STRING
def removeAllNonNumbersFromString(inputToProcess):
	logger.debug('#############################################START REMOVE ALL ALPHABET#############################################')

	cleanInput = removeAllControlCharacters(inputToProcess)
	
	cleanInput = cleanInput.strip()

	result = datetime.strptime(cleanInput, "%m/%d/%Y")
	
	logger.debug('Return value : %s',result)
		
	logger.debug('#############################################END REMOVE ALL ALPHABET#############################################')
	
	return result
	
	
## REMOVE ALL CONTROL CHARACTERES FROM STRING
def removeAllControlCharacters(stringToRemove):
	
	logger.debug('#############################################START REMOVE ALL CONTROL CHARACTERS##########')
		
	result = filter(string.printable.__contains__,stringToRemove)
	
	logger.debug("Return value : %s",result)

	logger.debug('#############################################END REMOVE ALL CONTROL CHARACTERS##########')
		
	return result


	
	
	


	
