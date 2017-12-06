# EXAMPLE
# Find out how many sentences in the US mainstream media that mentioned "Zimbabwe" and "president" in 2013:
# ```python
# import mediacloud, datetime
# mc = mediacloud.api.MediaCloud('MY_API_KEY')
# res = mc.sentenceCount('( zimbabwe AND president)', solr_filter=[mc.publish_date_query( datetime.date( 2013, 1, 1), datetime.date( 2014, 1, 1) ), 'tags_id_media:1' ])
# print res['count'] # prints the number of sentences found
# ```

## Initialize
import mediacloud, json, datetime, logging

#adding logging
logging.basicConfig(filename="logs.txt", level=logging.INFO)
logger = logging.getLogger("PS1") 

api_key = ""

#connect to media cloud
def make_media_cloud():
	mc = mediacloud.api.MediaCloud(api_key)
	if mc is not None:
		logger.info('connecting to mediacloud')
	else:
		logger.info('ERROR CONNECTING TO MEDIA CLOUD')
	return mc


## Research Question
## Which candidates did US Mainstream Media sources talk about more?

# ## Obama
# res = mc.sentenceCount('obama', solr_filter=[mc.publish_date_query( datetime.date( 2012, 9, 1), datetime.date( 2012, 9, 30) ), 'tags_id_media:1' ])
# print ("Obama: ", res['count']) # prints the number of sentences found

# ## Romney
# res = mc.sentenceCount('romney', solr_filter=[mc.publish_date_query( datetime.date( 2012, 9, 1), datetime.date( 2012, 9, 30) ), 'tags_id_media:1' ])
# print ("Romney: ", res['count']) # prints the number of sentences found

def fetch_candidate_data(name):
	mc = make_media_cloud()
	res = mc.sentenceCount(name, solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 9, 30) ), 'tags_id_media:1' ])
	logger.info(name + " : " + str(res['count']))
	return res['count']
	

## Trump
trumpy = fetch_candidate_data('trump')
print ("Trump: ", trumpy) # prints the number of sentences found 

## Clinton
clintony = fetch_candidate_data('clinton')
print ("Clinton: ", clintony) # prints the number of sentences found 



## Trump AND Russia over several months
# for x in range(3,11):

# 	res = mc.sentenceCount('(trump AND russia)', solr_filter=[mc.publish_date_query( datetime.date( 2017, x, 1), datetime.date( 2017, x, 30) ), 'tags_id_media:1' ])
# 	print ("Trump AND Russia during month of: ", (x), ": ", res['count']) # prints the number of sentences found 

