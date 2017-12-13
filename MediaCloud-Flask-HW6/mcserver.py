import configparser, logging, datetime, os, json

from flask import Flask, render_template, request

import mediacloud

CONFIG_FILE = 'settings.config'
basedir = os.path.dirname(os.path.realpath(__file__))

# load the settings file
config = configparser.ConfigParser()
config.read(os.path.join(basedir, 'settings.config'))

# set up logging
logging.basicConfig(level=logging.DEBUG)
logging.info("Starting the MediaCloud example Flask app!")

# clean a mediacloud api client
mc = mediacloud.api.MediaCloud(config.get('mediacloud','api_key') )
print(config.get('mediacloud','api_key'))



## change setting.config API_KEY to Heroku
## move API key to an evironmental variable

app = Flask(__name__)

##############################################################

## changing logging configuration
# if not app.debug and os.environ.get('HEROKU') is None:
#     import logging
#     from logging.handlers import RotatingFileHandler
#     file_handler = RotatingFileHandler('errors.log', 'a', 1 * 1024 * 1024, 10)
#     file_handler.setLevel(logging.INFO)
#     file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
#     app.logger.addHandler(file_handler)
#     app.logger.setLevel(logging.INFO)
#     app.logger.info('mediacloud app')

# if os.environ.get('HEROKU') is not None:
#     import logging
#     stream_handler = logging.StreamHandler()
#     app.logger.addHandler(stream_handler)
#     app.logger.setLevel(logging.INFO)
#     app.logger.info('mediacloud app')

# ### changing mediacloud settings.config api_key to heroku
# # heroku_api_key = os.environ.get('API_KEY')

# ### clean a mediacloud api client
# # mc = mediacloud.api.MediaCloud( heroku_api_key )
# mc = mediacloud.api.MediaCloud( config.get('mediacloud','api_key') )

# ##############################################################

@app.route("/")
def home():
    return render_template("search-form.html")

# turn data from this {'2016-10-04T00:00:00Z': 34, '2016-10-05T00:00:00Z': 57, '2016-10-06T00:00:00Z': 37
 # to looking like this  {"year": 1992, "name":"alpha", "value": 20},
def make_line_plot_data(results_data):
#  dates = [i[:10] for i in results_data.keys()]
  logging.debug("hellow 1")
  dates = results_data.keys()
  logging.debug("hellow")
  logging.debug([date for date in dates])
  sample_dates = [{"date" :  int("".join(date[:10].split("-"))), "name":"test", "value": results_data[date]} for date in dates if len(date) > 5]
  logging.info(sample_dates)
  return sample_dates

@app.route("/search",methods=['POST'])
def search_results():
    keywords = request.form['keywords']
    start_date = request.form['start_date']
    start_date_split = start_date.split('/')
    start_date_final = datetime.date(int(start_date_split[0]), int(start_date_split[1]), int(start_date_split[2]))
    print(start_date_final)

    end_date = request.form['end_date']
    end_date_split = end_date.split('/')
    end_date_final = datetime.date(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))
    print(end_date_final)

    results = mc.sentenceCount(keywords, 
      split = True, 
      split_start_date = "-".join(start_date_split), 
      split_end_date = "-".join(end_date_split),
      solr_filter=[mc.publish_date_query( start_date_final, end_date_final ),'tags_id_media:9139487'])

    logging.debug(results)
    data = make_line_plot_data(results['split'])
    logging.debug(json.dumps(data))
    return render_template("search-results.html",
                           keywords=keywords,
                           sentenceCount=results['count'], 
                           data = json.dumps(data, sort_keys=True), 
                           start_date = start_date, 
                           end_date = end_date )


# ### need to change for Heroku ###
# ### Heroku doesn't run, so have to pass through gunicorn ###
# if __name__ == "__main__":
#     #app.debug = True
#     app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)
#     #app.run()

if __name__ == "__main__":
  app.debug = True
  app.run()