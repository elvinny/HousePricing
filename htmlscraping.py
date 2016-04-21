#coding: utf8 
from bs4 import BeautifulSoup
import urllib
import logging
import logging.config
import os
import utility
import time
import database
import ssl


############################################LOGGING###############################################################################################
logging.config.fileConfig('logging_config.ini')
logger = logging.getLogger(os.path.basename(__file__))

############################################FUNCTIONS###############################################################################################

##GET NUMBER OF ROOMS
def getPropertyTitle(houseProperty):
	logger.debug('#############################################START GET PROPERTY TITLE#############################################')
	
	propertyTitle = houseProperty.find("p","searchPropertyTitle")
	logger.debug('Property Title: %s',propertyTitle)
	
	tagSpanPropertyTile = propertyTitle.find('span')
	result = tagSpanPropertyTile.text
	
	logger.info('Property Title value: %s',result)
	
	logger.debug('#############################################END GET PROPERTY TITLE#############################################')
	
	return result

##GET PROPERTY LOCATION	
def getPropertyLocation(houseProperty):
	logger.debug('#############################################START GET PROPERTY LOCATION#############################################')
	
	propertyLocation = houseProperty.find("p","searchPropertyLocation")
	logger.debug('Property Location: %s',propertyLocation)
	
	result = propertyLocation.text
	
	logger.info('Property Location value: %s',result)
	
	logger.debug('#############################################END GET PROPERTY LOCATION#############################################')
	
	return result

## GET PROPERTY PRICE
def getPropertyPrice(houseProperty):
	logger.debug('#############################################START GET PROPERTY PRICE#############################################')
	
	propertyPrice = houseProperty.find("div",class_="searchPropertyPrice")
	logger.debug('Property Price: %s',propertyPrice)
		
	tagSpanPropertyPrice = propertyPrice.find('span').contents[0]
	
	result = utility.removeStrangeChars(tagSpanPropertyPrice)
	
	logger.info('Property Price value: %s',result)
	
	logger.debug('#############################################END GET PROPERTY PRICE#############################################')
	
	return result

##GET LIST OF PAGES TO SCRAP
def getListOfPagesToScrap(numberOfPages):
	
	logger.debug('#############################################START GET LIST OF PAGES TO SCRAP#############################################')
	
	logger.debug('Number of Pages: %s',numberOfPages)
	
	baseString = 'https://casa.sapo.pt/Venda/Apartamentos/Lisboa/?sa=11'
	
	addString = '&pn='
	
	result = []
	
	##CHECK IF VALUE is a number
	try:
		
		i = float(numberOfPages)
    
	except (ValueError, TypeError):
		logger.warning('Number of pages is not numeric. Setting default value')
		numberOfPages = 100
    	
    	 
	if(numberOfPages <1  or numberOfPages =="" ):
		numberOfPages = 100
	
	
	for i in range(1,numberOfPages):
		concatenatedUrl = '{}{}{}'.format(baseString,addString,i)
		
		logger.debug('ConcatenatedUrl: %s',concatenatedUrl)
		
		result.append(concatenatedUrl)
						
	logger.debug('#############################################END GET LIST OF PAGES TO SCRAP#############################################')
	return result
	
## GET PROPERTY HTTP REFERENCE
def getPropertyHTTPRef(houseProperty):
	
	logger.debug('#############################################START GET HTTP REF#############################################')
			
	for link in houseProperty.find_all('a'):
		logger.debug('HTML Property HREF: %s',link.get('href'))
		result = link.get('href')
		break
			
	logger.debug('HTML Property: %s', result)
	
	return result
	
	logger.debug('#############################################END GET HTTP REF#############################################')
	

## GET PROPERTY FLOOR AREA (AREA UTIL) TODO
def getPropertyFloorArea(houseProperty):
	logger.debug('#############################################START GET PROPERTY FLOOR AREA#############################################')
			
	
	propertyInfo = houseProperty.find("div","searchPropertyInfo")
	
	previousTag = ''
	
	for divTags in propertyInfo.find_all('div'):
		for pTags in divTags.find_all('p'):
			logger.debug('PTags : %s', pTags.contents[0])		
					
			##PREVIOUS TAG is one of the ones we need to fetch, than let's pick the info
			if previousTag == 'estado':
				logger.debug('PreviousTag is %s',previousTag)
			elif previousTag == 'areautil':				
				logger.debug('PreviousTag is %s',previousTag)
			elif previousTag == 'areabruta':
				logger.debug('PreviousTag is %s',previousTag)
									
			previousTag = utility.remove_accents(pTags.contents[0])
			logger.debug('New previous Tag is : %s',previousTag)
									
		logger.debug('Search Property Info %s', divTags)		
		result = divTags.Text		
	logger.debug('#############################################END GET PROPERTY FLOOR AREA#############################################')
	
	
	return result

## GET PROPERTY PUBLISH DATE	
def getPropertyPublishDate(houseProperty):
	logger.debug('#############################################START GET PROPERTY PUBLISH DATE#############################################')
	
	propertyInfo = houseProperty.find("div",{"class":"searchPropertyDate"})
		
	logger.debug('Property Publish date HTML : %s', propertyInfo.contents[0])
		
	tempResult = utility.removeAllControlCharacters(propertyInfo.contents[0])

	tempResult = tempResult.split(" ")

	
	for value in tempResult:
		logger.debug('Split result : %s',value)
		result = value
	
	##cleaning again
	result = utility.removeAllControlCharacters(result)
		
	logger.debug('Property Publish clean date :%s', result)
	
	logger.debug('#############################################END GET PROPERTY PUBLISH DATE#############################################')
	
	return result

############################################MAIN###############################################################################################

start_time = time.time()

logger.debug('#############################################START HTML SCRAPING#############################################')

database_location = 'D:\\Scripts\\Project_House\\DB\\my_first_db.sqlite'

numberOfPages = 2
totalNumberOfProperties = 0

listOfPages = getListOfPagesToScrap(numberOfPages)

logger.info('Number of pages to Scrap: %s', numberOfPages)

for pageToScrap in listOfPages:

	logger.debug('#############################################START NEW PAGE TO SCRAP#############################################')
	logger.info('Page to Scrap: %s',pageToScrap)

	context = ssl._create_unverified_context()
	
	urlTestPage = urllib.urlopen(pageToScrap,context=context).read()
	
	soup = BeautifulSoup(urlTestPage,'lxml')

	logger.debug(soup.prettify()[1:1000])

	properties = soup.find_all("div", class_="searchResultProperty")

	#print type(properties)

	#iterate through properties
	for houseproperty in properties:
		
		logger.debug('Search Property HTML: %s' ,houseproperty.prettify()[0:1000])

		##GET SEARCH PROPERTY TITLE (EXAMPLE: Apartament T2, Apartamento T1)
		propertyTitleText = getPropertyTitle(houseproperty)		
			
		##GET SEARCH PROPERTY LOCATION (EXAMPLE: Av.EUA(alvalade), Alvalade,Lisboa)
		propertyLocationText = getPropertyLocation(houseproperty)
		
		##GET PROPERTY PRICE (300000,15000)
		propertyPriceText = getPropertyPrice(houseproperty)
		
		##GET PROPERTY HTML
		propertyHTMLRef = getPropertyHTTPRef(houseproperty)
		
		##GET PROPERTY INFO 
		propertyInfo = getPropertyFloorArea(houseproperty)
		
		#GET PROPERTY DATE
		propertyInfo = getPropertyPublishDate(houseproperty)
		
		
		logger.debug('Connection to DB with location %s:', database_location)
		connectionDB = database.connectDatabase(database_location)
		
		logger.debug('Connection to DB OK')
		
		if(database.insertIntoHistoryPrice(connectionDB,totalNumberOfProperties,propertyPriceText,propertyTitleText,propertyInfo,totalNumberOfProperties)):
			logger.debug('insert into History Price successfully')
		else:
			logger.debug('insert into History Price with issues. Please check')
		
		
		database.commitDatabase(connectionDB)
					
		totalNumberOfProperties+=1							
	
	logger.debug('#############################################END NEW PAGE TO SCRAP#############################################')
				
logger.debug('#############################################END HTML SCRAPING#############################################')

logger.info("Total number of properties: %s",totalNumberOfProperties)
logger.info("Total execution time of {} --- {}s seconds ---".format(__file__,(time.time() - start_time)))
				
