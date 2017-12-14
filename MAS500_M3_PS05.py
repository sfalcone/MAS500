#Initialize sqlalchemy
from sqlalchemy import *

## Initialize Media Cloud
import mediacloud, json, datetime

mc = mediacloud.api.MediaCloud('put your api key here')


## Research Question
## Which candidates did US Mainstream Media sources talk about more?

## Obama
res = mc.sentenceCount('obama', solr_filter=[mc.publish_date_query( datetime.date( 2012, 9, 1), datetime.date( 2012, 9, 30) ), 'tags_id_media:1' ])
print ("Obama: ", res['count']) # prints the number of sentences found
obama_count = res['count']
obama_row = {'keyword': 'obama', 'count': obama_count}
print(obama_row)

## Romney
res = mc.sentenceCount('romney', solr_filter=[mc.publish_date_query( datetime.date( 2012, 9, 1), datetime.date( 2012, 9, 30) ), 'tags_id_media:1' ])
print ("Romney: ", res['count']) # prints the number of sentences found
romney_count = res['count']
romney_row = {'keyword': 'romney', 'count': romney_count}
print(romney_row)

## Clinton
res = mc.sentenceCount('clinton', solr_filter=[mc.publish_date_query( datetime.date( 2012, 9, 1), datetime.date( 2012, 9, 30) ), 'tags_id_media:1' ])
print ("Clinton: ", res['count']) # prints the number of sentences found
clinton_count = res['count']
clinton_row = {'keyword': 'clinton', 'count': clinton_count}
print(clinton_row)
print("have media cloud date")

#Create a table 

# add `echo=True` to see log statements of all the SQL that is generated
engine = create_engine('sqlite:///:memory:',echo=True) # just save the db in memory for now (ie. not on disk)
metadata = MetaData()
# define a table to use
keywords_table = Table('queries', metadata,
    Column('id', Integer, primary_key=True),
    Column('keyword', String(400), nullable=False),
    Column('count', Integer, nullable=False),
    Column('timestamp', DateTime, default=datetime.datetime.now),
)

metadata.create_all(engine) # and create the tables in the databa
print("created table structure")

# Insert count per keyword
insert_stmt = keywords_table.insert().values([obama_row, romney_row, clinton_row])
db_conn = engine.connect()
result = db_conn.execute(insert_stmt)
searches_count = result.inserted_primary_key # print out the primary key it was assigned
print(searches_count)


from sqlalchemy.sql import select

select_stmt = select([keywords_table])
results = db_conn.execute(select_stmt)

total_calls = 0

for row in results:
	print(row)
	total_calls += row.count
    

print('total number of calls is: ')
print(total_calls)