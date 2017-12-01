# EXAMPLE
# Find out how many sentences in the US mainstream media that mentioned "Zimbabwe" and "president" in 2013:
# ```python
# import mediacloud, datetime
# mc = mediacloud.api.MediaCloud('MY_API_KEY')
# res = mc.sentenceCount('( zimbabwe AND president)', solr_filter=[mc.publish_date_query( datetime.date( 2013, 1, 1), datetime.date( 2014, 1, 1) ), 'tags_id_media:1' ])
# print res['count'] # prints the number of sentences found
# ```

## Initialize
import mediacloud, json, datetime

mc = mediacloud.api.MediaCloud("MY_API_KEY")


## Research Question
## Which candidates did US Mainstream Media sources talk about more?

## Obama
res = mc.sentenceCount('obama', solr_filter=[mc.publish_date_query( datetime.date( 2012, 9, 1), datetime.date( 2012, 9, 30) ), 'tags_id_media:1' ])
print ("Obama: ", res['count']) # prints the number of sentences found

## Romney
res = mc.sentenceCount('romney', solr_filter=[mc.publish_date_query( datetime.date( 2012, 9, 1), datetime.date( 2012, 9, 30) ), 'tags_id_media:1' ])
print ("Romney: ", res['count']) # prints the number of sentences found


## Trump
res = mc.sentenceCount('trump', solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 9, 30) ), 'tags_id_media:1' ])
print ("Trump: ", res['count']) # prints the number of sentences found 

## Clinton
res = mc.sentenceCount('clinton', solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 9, 30) ), 'tags_id_media:1' ])
print ("Clinton: ", res['count']) # prints the number of sentences found 

## Trump AND Russia over several months
for x in range(3,11):

	res = mc.sentenceCount('(trump AND russia)', solr_filter=[mc.publish_date_query( datetime.date( 2017, x, 1), datetime.date( 2017, x, 30) ), 'tags_id_media:1' ])
	print ("Trump AND Russia during month of: ", (x), ": ", res['count']) # prints the number of sentences found 

